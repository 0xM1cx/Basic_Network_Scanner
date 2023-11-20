#!bin/python3

import argparse
import re
import subprocess
from time import sleep
from scapy.all import Ether, srp, ARP

'''
TodoList:
1. Fix the calling pkt(str) python 3 makes no sense Suggestion -> Read the scapy documentation
'''

parser = argparse.ArgumentParser() # Initializes argparse

IP_Help = "Destination IP Address. E.g. 192.168.1.1 or 192.168.1.0/24"

parser.add_argument("-ip", type=str, required=True, help=IP_Help) # adds -ip arguments and sets it data type to strings and set to mandatory
args = parser.parse_args()

# ===== Scan Specific IP Address =====
class ScanSpecificAdd:
    def __init__(self, ip):
        arp = ARP(pdst=ip) # Creating an ARP Packet
        ether = Ether(dst="ff:ff:ff:ff:ff:ff") # Creating a broadcast Packet
        packet = ether/arp # Stacking the arp and ether Packets.

        result = srp(packet, timeout=3)[1]



# ===== Scan for IP Address range =====
class ScanSpecificSubnet:
    def __init__(self, ip):
        arp = ARP(pdst=ip) # Creating an ARP Packet
        ether = Ether(dst="ff:ff:ff:ff:ff:ff") # Creating a broadcast Packet
        packet = ether/arp # Stacking the arp and ether Packets.

        RESULTS = srp(packet, timeout=3)[0]
        CLIENTS = []
        for sent, received in RESULTS:
            CLIENTS.append({'ip': received.psrc, 'mac': received.hwsrc})
        
        # Print the hosts discovered in the network
        print(CLIENTS)

class Main:
    def __init__(self, ip):
        ListedAddress = re.split(r"[.|/]", args.ip) # Splits the ip address into 4 or 5 elements in a list.

        # ===== check if the input is in IP address format or not
        for address in ListedAddress:
            if int(address) in range(0,256) and len(ListedAddress) == 4 or len(ListedAddress) == 5:
                continue
            else:
                print("Follow the IP Address format")
                sleep(3)
                exit()

    

   

