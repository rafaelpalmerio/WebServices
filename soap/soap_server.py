from pytz import timezone
import pytz
from datetime import datetime

import logging
import os

from rpclib.application import Application
from rpclib.decorator import srpc
from rpclib.interface.wsdl import Wsdl11
from rpclib.protocol.soap import Soap11
from rpclib.service import ServiceBase
from rpclib.model.complex import Iterable
from rpclib.model.primitive import Integer
from rpclib.model.primitive import String
from rpclib.server.wsgi import WsgiApplication

class MessageService(ServiceBase):
    @srpc(String, Integer, _returns=Iterable(String))
    def send_message(msg, inteiro):
        yield 'Your message: %s' % msg

class tz(ServiceBase):
    @srpc(String, _returns=String)
    def get_time_in_tz(tz_name=''):
        if not tz_name:
            print('Você não especificou um fuso horário')
            return
        all_tz = pytz.all_timezones
        tz_matches = list(filter(lambda x: tz_name.lower().replace(' ','_') in x.lower(), all_tz))

        if tz_matches.__len__() >1:
            print('Foram encontrados ',tz_matches.__len__(),'fusos horários: \n')
        elif tz_matches.__len__()==1:
            print('Foi encontrado um fuso horário: \n')
        else:
            print('Não foi encontrado nenhum fuso horário.')
            return
        string = ''
        for tz in tz_matches:
            time_tz = timezone(tz)
            print(tz, ': ', str(datetime.now(time_tz)))
            string = string + tz + str(datetime.now(time_tz)) + '\n'
        return string
        

if __name__=='__main__':
    try:
      from wsgiref.simple_server import make_server
    except ImportError:
      print "Error: server requires Python >= 2.5"

    logging.basicConfig(level=logging.INFO)
    logging.getLogger('rpclib.protocol.xml').setLevel(logging.DEBUG)

    application = Application([tz], 'org.temporary.soap',
#               interface=Wsdl11(), 
                              in_protocol=Soap11(), out_protocol=Soap11())

    #   port = int(os.environ.get('PORT', 5000))
    port = 8000
    server = make_server('127.0.0.1', port, WsgiApplication(application))

    print "listening to http://127.0.0.1:%s" % port
    print "wsdl is at: http://127.0.0.1:%s/?wsdl" % port

    server.serve_forever()