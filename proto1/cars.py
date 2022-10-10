import pandas as pd
from enum import Enum
from typing import Any


class Brand:
    def __init__(self, *args: Any, **kwds: Any):
        pass


class Model(Enum):
    pass


class EngineType(Enum):
    COMBUSTION, ELECTRIC, HYBRID = 1, 2, 3


class Seats:
    def __init__(self, n_seats: int):
        self.n_seats = n_seats


class Car:
    def __init__(self, brand, model, seats, licencePlate, engineType: EngineType, current_autonomy, image):
        self.model = model
        self.brand = brand
        self.seats = seats
        self.licencePlate = licencePlate
        self.engineType = engineType
        self.current_autonomy = current_autonomy
        self.image = image  # image path


class CarPool(pd.DataFrame):
    def __init__(self, data):
        super().__init__(data)


class BMW (Car):
    def __init__(self):
        super().__init__(self, *args):
            self.brand = "BMW"
            self.model =
