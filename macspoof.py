#!/user/bin/env python
import subprocess

iface = input("Netwok Interface>")
addr = input("New MAC>")

subprocess.call("ifconfig " + iface + " down", shell=True)
subprocess.call("ifconfig " + iface + " hw ether " + addr, shell=True)
subprocess.call("ifconfig " + iface + " up", shell=True)