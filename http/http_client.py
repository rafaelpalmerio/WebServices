import requests

def _get(url):
    # faz uma requisição get
    session = requests.Session()
    return session.get(url).content

def _post(url, data):
    # faz uma requisição post
    session = requests.Session()
    return session.post(url, params=data).content
	

_get('https://wtfismyip.com/json')