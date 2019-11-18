import requests
class conexionauthserver :
    ip = '172.10.1.10' 
    puerto = '1234'
    def __init__(self,ip, puerto):
        ip = self.ip 
        puerto = self.puerto
        requests.get('http://'+ip+':'+puerto)

    def register(self,username,password):
        c = requests.post('http://'+self.ip+':'+self.puerto+'/user/create', data = {'username': username, 'password': password})
        return c.text

    def login(self,username,password):
        c = requests.post('http://'+self.ip+':'+self.puerto+'/user/login', data = {'username': username, 'password': password})
        return c.text 
    
    