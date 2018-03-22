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
        string = 'Foram encontrados '+ str(tz_matches.__len__()) + 'fusos horarios: \n'
    elif tz_matches.__len__()==1:
        string = 'Foi encontrado um fuso horario: \n'
    else:
        string = 'Nao foi encontrado nenhum fuso horario.'
    for tz in tz_matches:
        time_tz = timezone(tz)
        #print(tz, ': ', str(datetime.now(time_tz)))
        string = string + tz + str(datetime.now(time_tz)) + '\n'
    return string

serverSocket = socket(SOCK_DGRAM)
serverSocket.bind(('localhost', 5002))
serverSocket.listen(1)

def handler(c):
    while True:
        message = c.recv(1024).decode('utf-8')
        print(message)
        if 'close' in message:
            c.close()
            print('Fechando a conexao com um client')
            break
        response = get_time_in_tz(message).encode('ascii')
        c.send(response)

while True:
    c, address = serverSocket.accept()
    print('Conectado a um client')
    handler(c)
    