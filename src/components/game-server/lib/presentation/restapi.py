from flask import Flask, escape, request, abort

from lib.util.auth_server_util import authServerCon
from lib.util.hub_server_util import hubServerCon

import json

class RestApi():
    """ REST API facade.
    ---
    This class is a facade with the operations provided through the REST API.
    """
    def __init__(self):
        self.authCon = authServerCon()
        self.hubCon = hubServerCon()

    def status(self, request):
        """ Status handler.
        ---
        Always returns a tuple with the 200 status code and an "OK" message.
        """
        return (200, 'OK')

    def unirse(self, request):
        """ User creation handler.
        ---
        Performs the user creation operation, generating a new user in the database.

        Parameters:
            - request: The HTTP request received in the REST endpoint.
        Returns:
            A tuple with the following values:
                - (200, 'OK') on a successful creation.
                - (500, 'Server error') on a failed creation.
        """
        token = request.form['token']
        nombre = request.form['nombre']


        return (200, 'OK')

    def darDeAlta(self, request):
        """ User login handler.
        ---
        Performs the user login operation, generating a new token to be used in future operations.

        Parameters:
            - request: The HTTP request received in the REST endpoint.
        Returns:
            A tuple with the following values:
                - (200, authentication token) on a successful login.
                - (401, 'Unauthorized') on a failed login.
        """
        if self.hubCon.darDeAlta():
            return (200, 'OK')
        else:
            return (500, 'Error')

    def darDeBaja(self, request):
        """ Token checking handler.
        ---
        Checks the validity of an authentication token.

        Parameters:
            - request: The HTTP request received in the REST endpoint.
        Returns:
            A tuple with the following values:
                - (200, 'OK') when the provided token is valid.
                - (401, 'Unauthorized') for an incorrect token.
        """
        if self.hubCon.darDeBaja():
            return (200, 'OK')
        else:
            return (500, 'Error')

    def list_scores(self, request):
        """ Scores listing handler.
        ---
        Retrieves a list of scores.

        Parameters:
            - request: The HTTP request received in the REST endpoint.
        Returns:
            A tuple with the following values:
                - (200, list of score records) when the list was successfully retrieved.
        """
        db_session = SchemaManager.session()
        user_scores_rs = UserScores(db_session)
        user_score_records = user_scores_rs.get_all_user_scores()
        out = []
        for user_score_record in user_score_records:
            out.append({
                'username': user_score_record.username,
                'games_won': user_score_record.games_won,
                'games_lost': user_score_record.games_lost,
                'score': user_score_record.score
            })

        return (200, json.dumps(out))

    def add_score(self, request):
        """ Scores increasing handler.
        ---
        Increments (or decrements) the score of a user

        Parameters:
            - request: The HTTP request received in the REST endpoint.
        Returns:
            A tuple with the following values:
                - (200, 'OK') when the score was successfully updated.
                - (401, 'Unauthorized') when the user cannot update the scores.
        """
        token = request.form['token']
        games_won_delta = int(request.form['games_won']) if 'games_won' in request.form else None
        games_lost_delta = int(request.form['games_lost']) if 'games_lost' in request.form else None
        score_delta = int(request.form['score']) if 'score' in request.form else None

        db_session = SchemaManager.session()
        user_sessions_rs = UserSessions(db_session)
        if (not user_sessions_rs.token_is_valid(token)):
            return (401, 'Unauthorized')
        user_session = user_sessions_rs.get_session(token)
        
        user_scores_rs = UserScores(db_session)
        user_scores_rs.add_user_score(user_session.username, games_won_delta, games_lost_delta, score_delta)

        return (200, 'OK')
