import requests
class conexionauthserver :
    def __init__(self):
        self.ip = '172.10.1.10' 
        self.puerto = '1234'
        requests.get('http://'+self.ip+':'+self.puerto)

    def register(self,username,password):
        c = requests.post('http://'+self.ip+':'+self.puerto+'/user/create', data = {'username': username, 'password': password})
        return c.text

    def login(self,username,password):
        c = requests.post('http://'+self.ip+':'+self.puerto+'/user/login', data = {'username': username, 'password': password})
        return c.text 
    
    