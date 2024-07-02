#!/usr/bin/env python3

import netfilterqueue
import subprocess

subprocess.call(["iptables", "-I", "FORWARD", "-j", "NFQUEUE", "--queue-num", "0"])

def process_packet(packet):
    print(packet)
    packet.drop()

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()



subprocess.call(["iptables", "--flush"])
