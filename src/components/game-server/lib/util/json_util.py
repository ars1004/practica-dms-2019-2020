import json

def estado_a_json(estado):
    turno, tablero, fin = estado
    estado_dict = {'turno': turno, 'tablero': tablero, 'fin': fin}
    estado_json = json.dumps(estado)
    return estado_json

def json_a_movimiento(movimiento):
    mov = json.loads(movimiento)
    x,y = mov['x'], mov['y']
    return int(x), int(y)