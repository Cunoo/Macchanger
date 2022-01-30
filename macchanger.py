#!/bin/python3

import subprocess
import optparse
import re

def get_arguments():
	parser = optparse.OptionParser()
	parser.add_option("-i", "--interface", dest="interface", help="interface to change its MAC ADRESS")
	parser.add_option("-m", "--mac", dest="new_mac", help="New MAC ADRESS")
	(options, arguments) = parser.parse_args()
	if not options.interface:
		parser.error("[-] Please specifiy an interface, use --help for more info")
		
	elif not options.new_mac:
		parser.error("[-] Please specifiy an new mac address, use --help for more info")
	return options
		

def change_mac(interface,new_mac):
	print("-------Changing MAC ADDRES for " + interface + " to " + new_mac, "-------\n")

	subprocess.call(["ifconfig" ,interface,"down"])
	subprocess.call(["ifconfig" ,interface, "hw", "ether" ,new_mac])
	subprocess.call(["ifconfig" ,interface, "up"])

def get_current_mac(interface):
	ifconfig_result = subprocess.check_output(["ifconfig", interface])

	mac_addres_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result.decode("utf-8"))
	if mac_addres_result:
		return mac_addres_result.group(0)
	else:
		print("\n\nCould not read MAC addres!!!!!!")

options = get_arguments()

current_mac = get_current_mac(options.interface)
print("Current MAC : " + str(current_mac))
	
change_mac(options.interface, options.new_mac)

##Rewrite prevous variable
current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
	print("[+] MAC ADDRESS was succesfully changed to " + current_mac)
else:
	print("[-] MAC address did not get changed")
