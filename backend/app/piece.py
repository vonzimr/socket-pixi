from abc import ABC, abstractmethod

class Piece(ABC):

    def __init__(self, name, player):
        self.name = name
        self.player = player
        self.pos = [0,0]
        super().__init__()

    @property
    def get_name(self):
        return self.name

    @property
    def get_pos(self):
        return self.pos

    @property
    def get_player(self):
        return self.player

    def set_name(self, name):
        self.name = name
        return self.name

    def set_player(self, player):
        self.player = player

    @abstractmethod
    def set_pos(self, x, y):
        pass

    @abstractmethod
    def move_peice(self, x, y):
        pass
