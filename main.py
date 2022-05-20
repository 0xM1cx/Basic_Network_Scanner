import argparse
import re
import subprocess
from time import sleep
from colorama import Fore

parser = argparse.ArgumentParser() # Initializes argparse

IP_Help = "Destination IP Address. E.g. 192.168.1.1"

parser.add_argument("-ip", type=str, required=True, help=IP_Help) # adds -ip arguments and sets it data type to string and set to mandatory
args = parser.parse_args()

def scan(ip):
    # with open("log.txt", "a") as f:
    #     send = subprocess.check_output(["ping", "-c", "5", ip]).decode("utf-8")
    #     f.write(send) # Writes the ICMP echo reply to a log.txt file.
    subprocess.check_output(["ping", "-c", "5", ip]).decode("utf-8")
    




ListedAddress = re.split(r"[.|/]", args.ip) # Splits the ip address into 4 or 5 elements in a list.

for ip in ListedAddress:
    if int(ip) in range(0,256) and len(ListedAddress) == 4 or len(ListedAddress) == 5:
        continue
    else:
        print("Follow the IP Address format")
        sleep(5)
        exit()

try:
    scan(args.ip) # if the input is in IP address format they it will start scanning it.
    print(Fore.CYAN + "ONLINE" + Fore.WHITE)
except:
    print(Fore.RED + "OFFLINE" + Fore.WHITE)