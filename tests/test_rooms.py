import unittest

from lib.rooms import Room, rooms_builder

def count_rooms(starting_room, current_count=0):
    for room in starting_room.rooms.values():
        current_count = count_rooms(room, current_count+1)

    return current_count

class TestRooms(unittest.TestCase):
    def test_Room_init(self):
        room = Room()
        self.assertEqual(room.name, "")
        self.assertEqual(room.description, "")
        self.assertEqual(room.monster, None)
        self.assertEqual(room.items, [])

        room = Room(name="Cuthulu",
            description="This is a room",
            monster={},
            items=[1,2,3])
        self.assertEqual(room.name, "Cuthulu")
        self.assertEqual(room.description, "This is a room")
        self.assertEqual(room.monster, {})
        self.assertEqual(room.items, [1,2,3])

    def test_Room_draw(self):
        room = Room(name="Cuthulu",
            description="This is a room",
            monster={},
            items=[1,2,3])

        result = [
            "Room: {}".format("Cuthulu"),
            "\nDescription:\n{}".format("This is a room"),
        ]
        self.assertEqual(room.draw(), "\n".join(result))

    def test_Room_has_rooms(self):
        room = Room()
        self.assertIsInstance(room.rooms, dict)

    def test_rooms_builder(self):
        room = rooms_builder()
        self.assertIsInstance(room, Room)

    def test_rooms_builder_0_sub_rooms_default(self):
        starting_room = rooms_builder()

        room_count = 0

        for room in starting_room.rooms.values():
            room_count += 1

        self.assertEqual(room_count, 0)

    def test_rooms_builder_sub_rooms(self):
        starting_room = rooms_builder(number_sub_rooms=10)

        room_count = count_rooms(starting_room)

        self.assertEqual(room_count, 10)



