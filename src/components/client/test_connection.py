import requests

ip = '172.10.1.20'
puerto = '4567'
print('Obtener')
r = requests.get('http://'+ip+':'+puerto)
print(r.text)

name = 'servidor tanwsud tan chulo'
host = '172.10.1.30'
port = '9876'

c = requests.post('http://'+ip+':'+puerto+'/server/register', data = {'name': name, 'host': host, 'port': port})


c = requests.get('http://'+ip+':'+puerto+'/server', data = {'token': token})
print(c)
print(c.text)