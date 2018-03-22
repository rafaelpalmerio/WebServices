import socketserver, threading, time
from pytz import timezone
import pytz
from datetime import datetime


class ThreadedUDPRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        message = self.request[0].strip().decode('utf-8')
        socket = self.request[1]
        current_thread = threading.current_thread()
        response = get_time_in_tz(message).encode('ascii')
        print("{}: client: {}, wrote: {}".format(current_thread.name, self.client_address, response))
        socket.sendto(response, self.client_address)

class ThreadedUDPServer(socketserver.ThreadingMixIn, socketserver.UDPServer):
    pass

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
        print(tz, ': ', str(datetime.now(time_tz)))
        string = string + tz + str(datetime.now(time_tz)) + '\n'
    return string

if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 8080

    server = ThreadedUDPServer((HOST, PORT), ThreadedUDPRequestHandler)

    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True

    try:
        server_thread.start()
        print("Server started at {} port {}".format(HOST, PORT))
        while True: time.sleep(100)
    except (KeyboardInterrupt, SystemExit):
        server.shutdown()
        server.server_close()
        exit()