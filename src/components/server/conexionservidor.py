import requests
class conexionservidor:
    def __init__(self,ip,puerto):
        self.ip = ip
        self.puerto = puerto
        requests.get('http://'+ip+':'+puerto)
    def unirse(self,token,nombre):
        r = requests.post('http://'+self.ip+':'+self.puerto+'/unirse', data ={'token' : token, 'nombre' :nombre})
        return r.text
    def obtenerEstado(self):
        r = requests.get('http://'+self.ip+':'+self.puerto+'/estado')
        return r.text
    def obtenerJuegos(self):
        r = requests.get('http://'+self.ip+':'+self.puerto+'/obtener/juegos')
        return r.text
    def seleccionarJuego(self,token,juego):
        r = requests.post('http://'+self.ip+':'+self.puerto+'/seleccionar/juego', data = {'token':token,'juego':juego})
        return r.text
    def mover(self, token, movimiento):
        r = requests.post('http://'+self.ip+':'+self.puerto+'/mover', data = {'token':token,'movimiento':movimiento})
        return r.text