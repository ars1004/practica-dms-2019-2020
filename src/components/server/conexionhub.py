import requests
class conexionhub :
    ip = '172.10.1.20' 
    puerto = '4567'
    def __init__(self):
        requests.get('http://'+self.ip+':'+self.puerto)

    def obtenerLista(self,token):
        c = requests.get('http://'+self.ip+':'+self.puerto+'/server', data = {'token': token})
        return c.text

    
    