import time
from socket import *
import pytz
import random

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(3)

for pings in range(10000):
    
    #message = 'sao_paulo'
    message = random.choice(pytz.all_timezones)
    addr = ("127.0.0.1", 8080)

    start = time.time()
    clientSocket.sendto(message.encode('ascii'), addr)
    try:
        data, server = clientSocket.recvfrom(2048)
#         print(data.decode('utf-8'))
        end = time.time()
        elapsed = end - start
        print('%s %d %d' % (data, pings, elapsed))
    except timeout:
        print('REQUEST TIMED OUT')