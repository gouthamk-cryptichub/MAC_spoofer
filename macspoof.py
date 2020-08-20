#!/user/bin/env python
import subprocess

subprocess.call("ifconfig eth0 down", shell=True)
subprocess.call("ifconfig eth0 hw ether AA:BB:CC:DD:EE:FF", shell=True)
subprocess.call("ifconfig eth0 up", shell=True)