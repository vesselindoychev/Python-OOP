import datetime


class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        result = datetime.time(self.hours, self.minutes, self.seconds)
        return str(result)

    def next_second(self):
        if self.seconds == Time.max_seconds:
            self.seconds = 0
            if self.minutes == Time.max_minutes:
                self.minutes = 0
                if self.hours == Time.max_hours:
                    self.hours = 0
                else:
                    self.hours += 1
            else:
                self.minutes += 1
        else:
            self.seconds += 1
        return self.get_time()


time = Time(9, 30, 59)
print(time.next_second())
time = Time(10, 59, 59)
print(time.next_second())
time = Time(23, 59, 59)
print(time.next_second())


"""
from collections import deque


class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        result = f'{self.__return_hours()}:{self.__return_minutes()}:{self.__return_seconds()}'
        return result

    def next_second(self):
        result = deque()

        if self.seconds == Time.max_seconds:
            self.seconds = 0
            self.minutes += 1
        else:
            self.seconds += 1

        if self.minutes - 1 == Time.max_minutes:
            self.minutes = 0
            self.hours += 1

        if self.hours - 1 == Time.max_hours:
            self.hours = 0

        return self.get_time()

    def __return_hours(self):
        if self.hours < 10:
            return f'0{self.hours}'
        return self.hours

    def __return_minutes(self):
        if self.minutes < 10:
            return f'0{self.minutes}'
        return self.minutes

    def __return_seconds(self):
        if self.seconds < 10:
            return f'0{self.seconds}'
        return self.seconds

"""