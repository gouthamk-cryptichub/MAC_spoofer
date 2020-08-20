#!/user/bin/env python
import subprocess
import optparse

def get_args():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="iface", help="Name of the interface to change its MAC")
    parser.add_option("-m", "--mac", dest="addr", help="The new MAC Address")
    (value, args) = parser.parse_args()
    if not value.iface:
        parser.error("[-] ERROR Missing Interface name, use --help for more info")
    elif not value.addr:
        parser.error("[-] ERROR Missing new MAC Addr, use --help for more info.")
    return value
def change_mac(iface, addr):
    print("[+] Changing MAC Address of " + iface + "...")
    subprocess.call("ifconfig " + iface + " down", shell=True)
    subprocess.call("ifconfig " + iface + " hw ether " + addr, shell=True)
    subprocess.call("ifconfig " + iface + " up", shell=True)
    print("[+] Changed " + iface + "MAC Address to " + addr)

value = get_args()
change_mac(value.iface, value.addr)