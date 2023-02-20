class Room:
    def __init__(self, number, capacity):
        self.number = number
        self.capacity = capacity
        self.guests = 0
        self.is_taken = False

    def has_capacity(self, people):
        return not self.is_taken and self.capacity >= people

    def is_room_free(self):
        return self.is_taken

    def take_room(self, people):
        if not self.has_capacity(people):
            return f'Room number {self.number} cannot be taken'
        self.is_taken = True
        self.guests = people

    def free_room(self):
        if not self.is_room_free():
            return f'Room number {self.number} is not taken'
        self.is_taken = False
        self.guests = 0


#
# room = Room(1, 5)
# room2 = Room(2, 5)
# room3 = Room(3, 5)
# print(room.__dict__)
# print(room.take_room(4))
# print(room2.take_room(4))
# print(room2.take_room(10))
# print(room.free_room())
# print(room3.free_room())

