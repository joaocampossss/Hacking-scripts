#!/usr/bin/env python3

import scapy.all as scapy
import argparse

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--target', dest='target', help='Specify network to scan')
    options = parser.parse_args()
    if not options.target:
        parser.exit(1,'[-] Please specify a target network, use --help for more info\n')
    return options.target

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    clients_list = []

    for element in answered_list:
        client_dict = {'ip': element[1].psrc, 'mac': element[1].hwsrc}
        clients_list.append(client_dict)

    return clients_list

def print_result(results_list):
    print("IP\t\t\tMAC Address\n" + "-" * 80)
    for client in results_list:
        print(client['ip'] + "\t\t" + client['mac'])

options = get_arguments()
scan_result = scan(options)
print_result(scan_result)
