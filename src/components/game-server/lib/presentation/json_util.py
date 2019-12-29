import json


class JsonUtil:
    def estado_a_json(estado):
        """Pasa el estado a JSON
        El estado es una tupla con turno, tablero y fin de partida

        """
        turno, tablero, fin = estado
        estado_dict = {'turno': turno, 'tablero': tablero, 'fin': fin}
        estado_json = json.dumps(estado)
        return estado_json

    def json_a_movimiento(movimiento):
        """Pasa de un JSON a una tupla con el movimiento.
        El movimiento es una tupla con fila y columna.

        """
        mov = json.loads(movimiento)
        x, y = mov['x'], mov['y']
        return int(x), int(y)

    def objeto_a_json(objeto):
        return json.dumps(objeto)

    def json_a_objeto(json_str):
        return json.loads(json_str)
