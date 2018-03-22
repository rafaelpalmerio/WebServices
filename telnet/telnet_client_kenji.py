# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 20:15:34 2017

@author: Rafael
"""

import getpass
import sys
import telnetlib

HOST = "localhost"
HOST = '179.153.41.26'
PORT = '23'
#PORT = '8080'
user = input("Enter your remote account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST, PORT)

tn.read_until("login: ")
tn.write((user + "\n").encode('ascii'))
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")
    print(1)
tn.write("dir\n")
tn.write("exit\n")

print(tn.read_all())