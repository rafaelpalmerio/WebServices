import time
from socket import *
import random
import pytz

clientSocket = socket(SOCK_DGRAM)
clientSocket.connect(("127.0.0.1", 5002))
clientSocket.settimeout(1)
n = 999999
for pings in range(n): 
    #message = 'sao_paulo'
    message = random.choice(pytz.all_timezones)
    if pings == n-1:
        message = 'close'
    start = time.time()
    clientSocket.send(message.encode('ascii'))
    try:
        data = clientSocket.recv(1024)
#         print(data.decode('utf-8'))
        end = time.time()
        elapsed = end - start
        print('%s %d %d' % (data, pings, elapsed))
    except timeout:
        print('REQUEST TIMED OUT')