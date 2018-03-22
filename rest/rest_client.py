import httplib2
import json
import time
import datetime
a=True
if __name__ == '__main__':

    httplib2.debuglevel     = 0
    http                    = httplib2.Http()
    content_type_header     = "application/json"

    url = "http://127.0.0.1:5000/horario"

    data = {'tz_name':"sao paulo"}

    headers = {'Content-Type': content_type_header}
    print ("Posting %s" % data)

    while a:
        response, content = http.request( url,
                                          'POST',
                                          json.dumps(data),
                                          headers=headers)
        print (response)
        print (content)
        a=False
#         time.sleep(3)