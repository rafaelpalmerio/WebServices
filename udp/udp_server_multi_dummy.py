from socket import *

from pytz import timezone
import pytz
from datetime import datetime

def get_time_in_tz(tz_name=''):
    if not tz_name:
        string = 'Voce nao especificou um fuso horario'
        return
    all_tz = pytz.all_timezones
    tz_matches = list(filter(lambda x: tz_name.lower().replace(' ','_') in x.lower(), all_tz))
    string = ''
    if tz_matches.__len__() >1:
        string = 'Foram encontrados '+ str(tz_matches.__len__()) + 'fusos horários: \n'
    elif tz_matches.__len__()==1:
        string = 'Foi encontrado um fuso horario: \n'
    else:
        string = 'Nao foi encontrado nenhum fuso horario.'
    for tz in tz_matches:
        time_tz = timezone(tz)
        print(tz, ': ', str(datetime.now(time_tz)))
        string = string + tz + str(datetime.now(time_tz)) + '\n'
    return string

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('127.0.0.1', 8080))

while True:
    c, addr = serverSocket.accept()
    message, address = serverSocket.recvfrom(1024)
    message = message.decode('utf-8')
    response = get_time_in_tz(message).encode('ascii') 
    serverSocket.sendto(response, address) 