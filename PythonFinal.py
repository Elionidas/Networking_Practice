#!/usr/bin/env python

import os, glob, subprocess #HINT> MAJOR FRIGGIN HINT
import ctypes

"""
# Given a list of strings (['string1', 'string2', 'string3']), reverse all of the characters, and
# join them all together into a single string, with each previous word separated by spaces
# (the above example becomes '1gnirts 2gnirts 3gnirts')
"""
#define list of strings
StringList = ['string1', 'string2', 'string3']
def first_test(string_list):
    #first step, reverse the strings!
    #create a count for the list to stop the last value from having a space
    count = 0
    returnString = ""
    #for every string, reverse, add a space, then 
    for string in StringList:
        if count is len(StringList):
            Reverse = string[::-1]
            returnString += Reverse
        else:
            Reverse = string[::-1]
            Reverse += " "
            returnString += Reverse
        count += 1
    return returnString

print first_test(StringList)

#TEST ONE DONE
#MISSION PASSED: RESPECT+

"""
# Given a directory path, find each file that ends with '.txt', and create a dictionary,
# where each element consists of the filename, and its contents (e.g., if we had a file called
# "foo.txt" that contained "AAAA", our dictionary would look like: 
# { "evalFolder\\foo.txt" : "AAAA" }). This dictionary will be our return item.
"""
fileDict = "/home/student/evalFolder/"
returnDict = {}

def third_test(fname):
    #neat little trick to search a directory, finding all files with .txt
    #my directory happens to be in home/
    os.chdir(fileDict)
    for filename in glob.glob('*.txt'):
        print "opening " + filename  
        file = open(filename, "r")
        for line in file:
            returnDict.update({"evalfolder\\" + filename + ":" : line })
        #update that dictionary!
        file.close()
        continue
	return returnDict

print third_test(fileDict)
#print out the dictionary to show we read everything!
print returnDict
print "Found " + str(len(returnDict)) + " files with a .txt extension" #should be 18 values

#TEST 2 DONE
#MISSION PASSED: RESPECT+

#!/usr/bin/env python

'''
import socket, struct

dest = ('10.128.102.222', 1337)
accept_port_1 = 12345
accept_port_2 = 54321

cmd_list = {
	'success' : 0x800,
	'error' : 0x801,
	'query_mode' : 0x802,
	'get_key' : 0x803,
}

padding = 0x0000
'''

"""
  To accomplish this task, you will need to communicate with a server running on TCP port 1337 of 
 the grader system, using a fictional protocol. #DONE

-> Each command you issue will need to consist of a struct with two unsigned 32-bit longs, a command from the
cmd_list (above), and either an optional argument, or padding. #DONE

-> The grader expects to receive this in network byte order, and will return results in network
byte order (with the exception of the result you will get back from the get_key command).

-> The grader will give you back one of three types of results: 'success', 'error' (followed by
zeros if a generic error occurred, or all f's if an exception occurred while processing your request),
and finally, a 32 byte string (when the get_key command is successfully received).

-> Finally, the grader will only accept your commands if you set your source port to the value it 
is expecting (further explained in the task breakout below).

-> You will need to perform the following actions: 
1.) send a "query_mode" command to the server, using accept_port_1 as your source port
2.) send a "get_key" command to the server, with the mode you got back from the previous command,
using accept_port_2 as your source port.
"""
if __name__ == '__main__':
	pass

'''
We are gonna rewrite my performance lab to fulfill the needs of the final.
first off, we know we have a server to connect to.
so, the struct we are sending needs to contain two values, both of which need to be unsigned 32-bit longs.
for network byte order, which is big endian, the value for the unsigned long is 'L'
now, after that we need to send the struct(with packed values), to the specified destination.
'''

import socket, struct

dest = ('10.128.102.222', 1337)
accept_port_1 = 12345
accept_port_2 = 54321

cmd_list = {
	'success' : 0x800,
	'error' : 0x801,
	'query_mode' : 0x802,
	'get_key' : 0x803,
}

padding = 0x0000

#generate TCP client using IPv4
import ctypes
import struct
from socket import *

#write a TCP client server that packs the values and sends it to a server
c = socket(AF_INET, SOCK_STREAM)
#bind the first source_port
c.bind(("", 12345))
c.connect(dest)
#pack our struct
data = struct.pack('>LL', cmd_list['query_mode'], 0x0000)

c.send(data)

#receive the sent back data
data = c.recv(1024)
print struct.unpack('>LL', data)

#now to try the next one'
import socket, struct

dest = ('10.128.102.222', 1337)
accept_port_1 = 12345
accept_port_2 = 54321

cmd_list = {
	'success' : 0x800,
	'error' : 0x801,
	'query_mode' : 0x802,
	'get_key' : 0x803,
}

padding = 0x0000

#generate TCP client using IPv4
import ctypes
import struct
from socket import *

#write a TCP client server that packs the values and sends it to a server
c = socket(AF_INET, SOCK_STREAM)
#bind the first source_port
c.bind(("", 54321))
c.connect(dest)

data = struct.pack('>LL', cmd_list['get_key'], 12648430)

c.send(data)

data = c.recv(1024)

#pack with query mode, should get back information, unpack, and then split the information?

#server ip: 192.168.206.158