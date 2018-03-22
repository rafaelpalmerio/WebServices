#!flask/bin/python
from flask import Flask, request, jsonify
from pytz import timezone
import pytz
from datetime import datetime

app = Flask(__name__)

@app.route('/horario', methods=['POST'])
def get_time_in_tz():
    tz_name=request.json['tz_name']
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
    for tz in tz_matches:
        time_tz = timezone(tz)
        print(tz, ': ', str(datetime.now(time_tz)))

    return jsonify({tz: str(datetime.now(timezone(tz))) for tz in tz_matches}), 201

if __name__ == '__main__':
    print 'iniciando o servidor'
    app.run(port=5000, debug=False)