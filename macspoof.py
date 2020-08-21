#!/user/bin/env python
import subprocess
import optparse
import re

def get_mac(iface):
    try:
        mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w", subprocess.check_output(["ifconfig", iface]))
    except:
        print("[-] Interface not valid, Please check the interface name.")
        exit()
    if mac:
        return mac.group(0)
    else:
        print("[-] ERROR MAC address not found.")
def get_args():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="iface", help="Name of the interface to change its MAC")
    parser.add_option("-m", "--mac", dest="addr", help="The new MAC Address")
    (value, args) = parser.parse_args()
    if not value.iface:
        parser.error("[-] ERROR Missing Interface name, use --help for more info.")
    elif not value.addr:
        parser.error("[-] ERROR Missing new MAC Addr, use --help for more info.")
    return value
def change_mac(iface, addr):
    print("[+] Changing MAC Address of " + iface + "...")
    try:
        subprocess.call("ifconfig " + iface + " down", shell=True)
        subprocess.call("ifconfig " + iface + " hw ether " + addr, shell=True)
        subprocess.call("ifconfig " + iface + " up", shell=True)
    except:
        print("[-]An error occured unable to change MAC address.")
        exit()

value = get_args()
print("[+] Current MAC address of " + value.iface + " is " + get_mac(value.iface))
change_mac(value.iface, value.addr)
print("[+] Successfully changed MAC address of " + value.iface + " to " + get_mac(value.iface))
