import argparse
import re
import subprocess
from time import sleep

parser = argparse.ArgumentParser() # Initializes argparse

parser.add_argument("-ip", type=str, required=True) # adds -ip arguments and sets it data type to string and set to mandatory
args = parser.parse_args()

def scan(ip):
    with open("log.txt", "a") as f:
        send = subprocess.check_output(["ping", "-c", "5", ip]).decode("utf-8")
        f.write(send) # Writes the ICMP echo reply to a log.txt file.


# 1. Fix the slash notation because it can't go beyond /4


add = re.split(r"[.|/]", args.ip) # Splits the ip address into 4 or 5 elements in a list.

for ip in add:
    if int(ip) in range(0,256) and len(add) == 4 or len(add) == 5:
        continue
        # if re.search(r"/[]$", args.ip ):
    else:
        print("Follow the IP Address format")
        sleep(5)
        exit()

scan(args.ip)
