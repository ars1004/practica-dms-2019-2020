import requests
class conexionhub :
    ip = '172.10.1.20' 
    puerto = '4567'
    def __init__(self):
        ip = self.ip 
        puerto = self.puerto
        requests.get('http://'+ip+':'+puerto)

    def obtenerLista(self,token):
        c = requests.get('http://'+self.ip+':'+self.puerto+'/server', data = {'token': token})
        return c.text

    
    