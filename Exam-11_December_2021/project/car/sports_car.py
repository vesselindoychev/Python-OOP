from project.car.car import Car


class SportsCar(Car):
    _MIN_SPEED_LIMIT = 400
    _MAX_SPEED_LIMIT = 600
    _INVALID_SPEED_MESSAGE = f"Invalid speed limit! Must be between {_MIN_SPEED_LIMIT} and {_MAX_SPEED_LIMIT}!"


    def __init__(self, model, speed_limit):
        super().__init__(model, speed_limit)
