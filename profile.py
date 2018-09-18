import geni.portal as portal
import geni.rspec.pg as rspec

request = portal.context.makeRequestRSpec()

node1 = request.XenVM("node-1")
iface1 = node1.addInterface("if1")  

pool = AddressPool( "poolname", 3 )
rspec.addResource( pool )

# Specify the component id and the IPv4 address
iface1.component_id = "eth1"
iface1.addAddress(rspec.IPv4Address("192.168.1.1", "255.255.255.0"))

node2 = request.XenVM("node-2")
iface2 = node2.addInterface("if2")

# Specify the component id and the IPv4 address
iface2.component_id = "eth2"
iface2.addAddress(rspec.IPv4Address("192.168.1.2", "255.255.255.0"))

node2 = request.XenVM("node-3")
iface2 = node2.addInterface("if3")

# Specify the component id and the IPv4 address
iface2.component_id = "eth3"
iface2.addAddress(rspec.IPv4Address("192.168.1.3", "255.255.255.0"))

node2 = request.XenVM("node-4")
iface2 = node2.addInterface("if4")

# Specify the component id and the IPv4 address
iface2.component_id = "eth4"
iface2.addAddress(rspec.IPv4Address("192.168.1.4", "255.255.255.0"))
 
# Add a raw PC to the request.
node = request.RawPC("node-1")
node = request.RawPC("node-2")
node = request.RawPC("node-3")
node = request.RawPC("node-4")

# Install and execute scripts on the node. THIS TAR FILE DOES NOT ACTUALLY EXIST!
node.addService(rspec.Install(url="http://example.org/sample.tar.gz", path="/local"))
node.addService(rspec.Execute(shell="bash", command="/local/example.sh"))

portal.context.printRequestRSpec()

link = request.LAN("lan")

link.addInterface(iface1)
link.addInterface(iface2)
link.addInterface(iface3)
link.addInterface(iface4)

portal.context.printRequestRSpec()
