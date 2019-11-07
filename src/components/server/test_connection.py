import requests

ip = '172.10.1.20'
puerto = '4567'

r = requests.get('http://'+ip+':'+puerto)
print(r.text)

name = 'servidor no tan chulo'
host = '123.456.789.012'
port = '7654'

c = requests.post('http://'+ip+':'+puerto+'/server/register', data = {'name': name, 'host': host, 'port': port})

token = 'd4cfa322-ab17-4d33-8ed6-ede0061b8600'

c = requests.get('http://'+ip+':'+puerto+'/server', data = {'token': token})

print(c)
print(c.text)