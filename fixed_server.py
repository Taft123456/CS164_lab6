import socket
import sys
import time
from check import ip_checksum
import random

HOST = ''
PORT = 8304

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind((HOST,PORT))

print "Created Socket and bind"

while 1:
        d = s.recvfrom(1024)
        data = d[0]
        addr = d[1]

        if not d:
                break

        packet = 'Sending packet'
        s.sendto(packet,addr)

        print data

        delay = random.random() * 2
        time.sleep(delay)

s.close()