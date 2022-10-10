import re
from dataclasses import dataclass
from enum import Enum
from typing import Any

import pandas as pd

# from wand.image import Image

class EngineType(Enum):
    COMBUSTION, ELECTRIC, HYBRID = 1, 2, 3
    
class BMWModel(Enum):
    pass

@dataclass
class Car:
        brand: str
        model: str
        seats: int
        licence_plate: str #TODO: format string to plate_format = re.compile([0-9]{2}[\s-]{0,1}[0-9]{2}[\s-]{0,1}[A-IK-PR-VZ]{2}|[0-9]{2}[\s-]{0,1}[A-IK-PR-VZ]{2}[\s-]{0,1}[0-9]{2}|[A-IK-PR-WYZ]{2}[\s-]{0,1}[0-9]{2}[\s-]{0,1}[A-IK-PR-WYZ]{2})
        engine_type: EngineType
        current_autonomy: int
        image: str  # image path TODO: assign Blob type to image attibute

class BMW (Car):
    brand: str = "BMW"
    # model: 



class CarPool(pd.DataFrame):
    def __init__(self, data):
        super().__init__(data)


# class BMW (Car):
#     def __init__(self):
#         super().__init__(self, *args):


# class Brand:
#     def __init__(self, *args: Any, **kwds: Any):
#         pass


# class Model:





# class Seats:
#     def __init__(self, n_seats: int):
#         self.n_seats = n_seats