"""
Lab 3A.py
Name: Elias Perez
Date: September 14th, 2018
"""

'''
Using the struct package from the python library, pack the values (1, 2, -3, -4) as the following data types (unsigned short, unsigned int, signed short, signed int)
1 as an unsigned short
2 as an unsigned int
-3 as a signed short
-4 as a signed int
Write a TCP client that packs those values, sends the packed string to a server.
Write a TCP server that receives the string, unpacks it using little endian and prints it, then unpacks it again using big endian and prints it.
'''

import ctypes
import struct
from socket import *

data = struct.pack('=HIhi', 1, 2, 3, 4)

#write a TCP client server that packs the values and sends it to a server

c = socket(AF_INET, SOCK_STREAM)
c.connect(("",15000))
c.send(data)

# write a TCP Server, that receives the string, 
# unpacks it using little endian and prints it, 
# then unpacks it again and uses big endian and prints it.

from socket import *
import struct
import ctypes

s = socket(AF_INET, SOCK_STREAM)
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(("", 15000))
s.listen(1)
c, a = s.accept()
data = c.recv(1024)

print struct.unpack('<Hihi', data)
print struct.unpack('>HIhi', data)