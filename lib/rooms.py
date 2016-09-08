
class Room():
    def __init__(self,
        name="",
        description="",
        monster=None,
        items=None,
        rooms=None):
        
        self.name = name
        self.description = description
        self.monster = monster
        self.items = items or []
        self.rooms = rooms or {}

    def draw(self):
        """
        Outputs information for the user to be able to
        visualize the room they are currently in
        """

        room_output = [
            "Room: {}".format(self.name),
            "\nDescription:\n{}".format(self.description),
        ]

        return "\n".join(room_output)

def add_rooms(room, number_rooms_left=0):
    directions = [
        'north',
        'south',
        'east',
        'west',
    ]

    current_rooms_left = number_rooms_left

    if current_rooms_left > 0:
        for direction in directions:
            current_rooms_left -= 1
            room.rooms[direction] = add_rooms(Room(), current_rooms_left)

            if (current_rooms_left <= 0):
                break

    return room

def rooms_builder(number_sub_rooms=0):
    """
    Returns a starting room that contains
    a tree of rooms off the starting room
    """

    starting_room = Room(
        name="Starting Point",
        description="This is the first room")

    starting_room = add_rooms(starting_room, number_sub_rooms)

    #TODO: build tree of rooms off of starting room

    return starting_room