"""
Performance_Lab_4-2.py
Name: Elias Perez
Date: September 26th, 2018
"""

'''
Create a TCP client using IPv4. 
Pack the following values in a struct using network byte order:
 12345, 56789, &, *, 0x7d0, 0b11111010000. 
 Then send the packed struct to a TCP server, 
 and print the unpacked values.
'''

#generate TCP client using IPv4
import ctypes
import struct
import binascii
from socket import *

#using ord() allows ascii to be seen as integers, 
# and python can automatically convert other forms of a digit 
# into an int by casting, as long as the full number is there
data = struct.pack('>iiiiii', 12345, 5678, ord('&'), ord('*'), int(0x7d0), int(0b11111010000))

#write a TCP client server that packs the values and sends it to a server
c = socket(AF_INET, SOCK_STREAM)
c.connect(("",15000))
c.send(data)

#write a TCP server that unpacks the struct in network byte order
#(more commonly known as big endian!)
from socket import *
import struct
import ctypess

s = socket(AF_INET, SOCK_STREAM)
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(("", 15000))
s.listen(1)
c, a = s.accept()
data = c.recv(1024)

print struct.unpack('>iiiiii', data)