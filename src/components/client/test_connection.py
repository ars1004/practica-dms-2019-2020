import requests

ip = '172.10.1.20'
puerto = '4567'
r = requests.get('http://'+ip+':'+puerto)

name = 'Servidor 0'
host = '172.10.1.30'
port = '9876'

c = requests.post('http://'+ip+':'+puerto+'/server/register', data = {'name': name, 'host': host, 'port': port})
