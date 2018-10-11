from backend.app.board import Board


class Room:
    def __init__(self, lobby_id, name):
        self._board = Board()
        self._players = {}
        self.name = name

    def add_player(self, player):
        self._players[player.cid] = player

    @property
    def num_players(self):
        return len(self._players.keys())

    def __repr__(self):
        players = "".join(["{}, ".format(player.player_name) for player in self._players.values()])
        return "{}|{}".format(self.name, players)

    def save_room(self):
        """
        Save the current Room state to some databse or something?
        :return:
        """
        pass
