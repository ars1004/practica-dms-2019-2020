import requests

ip = '172.10.1.10'
puerto = '1234'

r = requests.get('http://'+ip+':'+puerto)
print(r.text)


usuario = 'asdfasdfas'
password = '12341234'

c = requests.post('http://'+ip+':'+puerto+'/user/create', data = {'username': usuario, 'password': password})

c = requests.post('http://'+ip+':'+puerto+'/user/login', data = {'username': usuario, 'password': password})

print(c)
print(c.text)