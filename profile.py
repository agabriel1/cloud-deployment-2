"""This is a 4 node cluster deployed to cloudlab; The profile source code and other software, documentation, etc. are stored in in a publicly accessible GIT repository (say, github.com). When you instantiate this profile, the repository is cloned to all of the nodes in your experiment, to `/local/repository`. 
This particular profile is a simple example of using a single raw PC. It can be instantiated on any cluster; the node will boot the default operating system, which is typically a recent version of Ubuntu.
Instructions:
Wait for the profile instance to start, then click on the node in the topology and choose the `shell` menu item. 
"""
# Import the Portal object.
import geni.portal as portal
# Import the ProtoGENI library
import geni.rspec.pg as rspec
request = portal.context.makeRequestRSpec()
node1 = request.XenVM("node1")
iface1 = node1.addInterface("if1")
node1.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:CENTOS7-64-STD"
node1.routable_control_ip = "true"
 # Specify the component id and the IPv4 address
iface1.component_id = "eth1"
iface1.addAddress(rspec.IPv4Address("192.168.1.1", "255.255.255.0"))
node2 = request.XenVM("node2")
iface2 = node2.addInterface("if2")
node2.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:CENTOS7-64-STD"
 # Specify the component id and the IPv4 address
iface2.component_id = "eth2"
iface2.addAddress(rspec.IPv4Address("192.168.1.2", "255.255.255.0"))
node3 = request.XenVM("node3")
iface3 = node3.addInterface("if3")
node3.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:CENTOS7-64-STD"
 # Specify the component id and the IPv4 address
iface3.component_id = "eth3"
iface3.addAddress(rspec.IPv4Address("192.168.1.3", "255.255.255.0"))
node4 = request.XenVM("node4")
iface4 = node4.addInterface("if4")
node4.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:CENTOS7-64-STD"
 # Specify the component id and the IPv4 address
iface4.component_id = "eth4"
iface4.addAddress(rspec.IPv4Address("192.168.1.4", "255.255.255.0"))
portal.context.printRequestRSpec()
link = request.LAN("lan")
link.addInterface(iface1)
link.addInterface(iface2)
link.addInterface(iface3)
link.addInterface(iface4)
portal.context.printRequestRSpec()
