#!/user/bin/env python
import subprocess
import optparse

parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest="iface", help="Name of the interface to change its MAC")
parser.add_option("-m", "--mac", dest="addr", help="The new MAC Address")
(value, args) = parser.parse_args()

subprocess.call("ifconfig " + value.iface + " down", shell=True)
subprocess.call("ifconfig " + value.iface + " hw ether " + value.addr, shell=True)
subprocess.call("ifconfig " + value.iface + " up", shell=True)