from Exams.project import Room


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0
        self.taken_rooms = []

    @classmethod
    def from_stars(cls, start_count):
        return cls(f'{start_count} stars Hotel')

    def _get_room_by_number(self, room_number):
        possible_rooms = [r for r in self.rooms if r.number == room_number]
        return possible_rooms[0]

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        room = self._get_room_by_number(room_number)

        if room.take_room(people):
            return
        self.guests += people

    def free_room(self, room_number):
        room = self._get_room_by_number(room_number)

        if room.free_room():
            return
        self.guests -= room.guests

    def status(self):
        free_rooms = [str(r.number) for r in self.rooms if not r.is_taken]
        taken_rooms = [str(r.number) for r in self.rooms if r.is_taken]
        return f'Hotel {self.name} has {self.guests} total guests\n' \
               f'Free rooms: {", ".join(free_rooms)}\n' \
               f'Taken rooms: {", ".join(taken_rooms)}'


hotel = Hotel.from_stars(5)

first_room = Room(1, 3)
second_room = Room(2, 2)
third_room = Room(3, 1)

hotel.add_room(first_room)
hotel.add_room(second_room)
hotel.add_room(third_room)

hotel.take_room(1, 4)
hotel.take_room(1, 2)
hotel.take_room(3, 1)
hotel.take_room(3, 1)

print(hotel.status())
