class Piece:

    def __init__(self, name, player):
        self.name = name
        self.player = player
        self.pos = (,)

    @property
    def get_name(self):
        return self.name

    @property
    def get_pos(self):
        return self.pos

    @property
    def get_player(self):
        return self.player

    def move_peice(self, x, y):
        
