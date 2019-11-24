
class PlayerUtil:
    player_to_token_dict = {}
    token_to_player_dict = {}
    
    def add_player(self, token, player):
        """Añade un jugador.


        """
        self.player_to_token_dict[player] = token
        self.token_to_player_dict[token] = player

    def token_to_player(self, token):
        """Obtiene el jugador correspondiente al token.
        """
        return self.token_to_player_dict[token]

    def player_to_token(self, player):
        """Obtiene el token correspondiente al jugador.
        """
        return self.player_to_token_dict[player]