#!/usr/bin/env python
import subprocess
import optparse as opt

def change_mac(interface, new_mac):
    print("[+] Changing MAC address for "+ interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_args():
    parser = opt.OptionParser()
    parser.add_option("-i", "--interface", dest = "interface", help = "Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest = "new_mac", help = "New MAC address")
    (options, args) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Pease specify an interface, use --help for more info.")
    if not options.new_mac:
        parser.error("[-] Pease specify a new mac, use --help for more info.")
    return options


options = get_args()
change_mac(options.interface, options.new_mac)