from socket import timeout
import socket
import sys
import time
from check import ip_checksum
import random

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host='localhost'
port = 8304

s.settimeout(1)
numSent = 0
window_group = 0
temp = ''
msg = raw_input('Enter message to send: ')

for i in range(20):
        error = random.random()
        if temp.startswith('Timeout'):
                s.sendto('Packet out of order', (host, port))
        elif temp.startswith('Sending'):
                s.sendto('Checksum:\nThe checksums match', (host, port))
        else:
                s.sendto('', (host, port))
        try:
                d = s.recvfrom(1024)
                receive = d[0]
                if numSent % 4 == 0:
                        if i > 0 and numSent > 0:
                                print 'Server reply: ACK' + str(window_group)
                                window_group = window_group + 1
                        print 'Checksum:'
                print receive + str(numSent)
                numSent = numSent + 1
                temp = receive + temp

        except timeout:
                print 'Timeout'
                print 'Resending the packet'
                temp = 'Timeout' + temp