from suds.client import Client
url = 'http://localhost:8000/tz?wsdl'
client1 = Client(url)
client1.service.get_time_in_tz("America")