
class ListaJugadores:
    jugador_a_token_dict = {}
    token_a_jugador_dict = {}
    
    def añadir_jugador(self, token, player):
        """Añade un jugador.
        """
        self.jugador_a_token_dict[player] = token
        self.token_a_jugador_dict[token] = player

    def obtener_jugador(self, token):
        """Obtiene el jugador correspondiente al token.
        """
        return self.token_a_jugador_dict[token]

    def obtener_token(self, player):
        """Obtiene el token correspondiente al jugador.
        """
        return self.jugador_a_token_dict[player]

    def obtener_numero_jugadores(self):
        return len(self.jugador_a_token_dict)
    
    def vaciar(self):
        self.jugador_a_token_dict.clear()
        self.token_a_jugador_dict.clear()