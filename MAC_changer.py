#!/usr/bin/env python3

from random import randint
import subprocess
import optparse 
import re

def get_arguments():
	parser = optparse.OptionParser()
	parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address.")
	parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
	(options, arguments) = parser.parse_args()
	if not options.interface:
		parser.error("[-] Please specify an interface, use --help for more info.")
	elif not options.new_mac:
		options.new_mac = generate_mac()
	return options


def generate_mac():
	mac = "02:%02x:%02x:%02x:%02x:%02x" % (randint(0, 255),
                             randint(0, 255),
                             randint(0, 255),
                             randint(0, 255),
                             randint(0, 255))

	return mac


def change_mac(interface, new_mac):
	subprocess.call(['ifconfig', interface, 'down'])
	subprocess.call(['ifconfig', interface, 'hw', 'ether', new_mac])
	subprocess.call(['ifconfig', interface, 'up'])
	print(f"[+] Changed MAC address for {interface} to {new_mac}")


def find_mac(interface):
	parser = optparse.OptionParser()
	
	try:
		ifconfig_result = subprocess.check_output(["ifconfig", interface])
	except subprocess.CalledProcessError:
		quit()

	mac = re.search(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w', str(ifconfig_result))
	mac = mac.group(0)
	return mac


def main():
	options = get_arguments()
	if find_mac(options.interface) == options.new_mac:
		parser = optparse.OptionParser()
		parser.error("[-] You already have this MAC address.")
	else:
		change_mac(options.interface, options.new_mac)


if __name__ == '__main__':
	main()

