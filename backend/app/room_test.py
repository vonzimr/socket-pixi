from unittest import TestCase
from unittest.mock import Mock
from backend.app.room import Room


class RoomTests(TestCase):

    def setUp(self):
        self.fake_id = "fake"
        self.name = "My Fake Room"
        self.room = Room(self.fake_id, self.name)

    def test_num_players_prop(self):
        p = Mock()
        p.name = 'fake_name'
        p.id = 'fake_id'
        self.room.add_player(p)
        self.assertEqual(self.room.num_players, 1)

    def test_room_repr(self):
        p = Mock()
        p.name = 'fake_name'
        p.id = 'fake_id'
        self.room.add_player(p)
        self.assertEqual(str(self.room), "{}|{}".format(self.name, p.name))

    def test_room_repr_multiple_players(self):
        p1 = Mock()
        p1.name = 'fake_name'
        p1.id = 'fake_id'

        p2 = Mock()
        p2.name = 'another_fake_name'
        p2.id = 'fake_id'
        self.room.add_player(p1)
        self.room.add_player(p2)
        self.assertEqual("{}|{},{}".format(self.name, p1.name, p2.name), str(self.room))
