class Account:
    def __init__(self, id, balance, pin):
        self.id = id
        self.balance = balance
        self.pin = pin

    def get_id(self, pin):
        if not self.pin == pin:
            return f'Wrong pin'
        return self.id

    def change_pin(self, old_pin, new_pin):
        if not self.pin == old_pin:
            return f'Wrong pin'
        self.pin = new_pin
        return f'Pin changed'

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def pin(self):
        return self.__pin

    @pin.setter
    def pin(self, value):
        self.__pin = value


account = Account(8827312, 100, 3421)
print(account.get_id(1111))
print(account.get_id(3421))
print(account.balance)
print(account.change_pin(2212, 4321))
print(account.change_pin(3421, 1234))
