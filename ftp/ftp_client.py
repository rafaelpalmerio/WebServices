# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 17:23:28 2017

@author: Rafael
"""

import os
from ftplib import FTP

ftp = FTP()
ftp.connect('localhost',8888)
ftp.login('rafael', '12345')

os.chdir(r'C:\Users\Rafael\Documents\ftp_test\\')
#ftp.cwd(r'C:\Users\Rafael\Documents\ftp_test')

def grabFile():
    filename = 'file_teste.txt'
    localfile = open(filename, 'wb')
    ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
    
    ftp.quit()
    localfile.close()

def placefile():
    filename = 'filte_teste.txt'
    ftp.storbinary('STOR ' + filename, open(filename, 'rb'))
    ftp.quit()

if __name__ == "__main__":
    grabFile()