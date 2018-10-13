from unittest import TestCase
from backend.app.room import Room
from backend.app.player import Player


class RoomTests(TestCase):

    def setUp(self):
        self.fake_id = "fake"
        self.name = "My Fake Room"
        self.room = Room(self.fake_id, self.name)

    def test_num_players_prop(self):
        p = Player('11111', 'fake_name')
        self.room.add_player(p)
        self.assertEqual(self.room.num_players, 1)


    def test_room_repr(self):
        p = Player('11111', 'fake_name')
        self.room.add_player(p)
        self.assertEqual(str(self.room), "{}|{}".format(self.name, p.name))

