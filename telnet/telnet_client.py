# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 19:53:30 2017

@author: Rafael
"""

import telnetlib

HOST = "localhost"
#HOST = '179.153.41.26'
#PORT = '23'
PORT = '8080'

tn = telnetlib.Telnet(HOST, PORT)

while True:
    msg = input("Digite uma mensagem para o servidor: ")    
    tn.write((msg + "\n").encode('ascii'))
