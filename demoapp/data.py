
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

Base = automap_base()

engine = create_engine("mysql+pymysql://app:appass@127.0.0.1:3306/carPoolDB")

Base.prepare(engine, reflect=True, schema='carPoolDB')
AllCars = Base.classes.allCarOptions
CarPool = Base.classes.carPool
Booking = Base.classes.reservations
Drivers = Base.classes.drivers

session = Session(engine)

# # session.add(Drivers(driverName="Jaquim", driverPhone="234567890",
# #             driverEmail="Jota@gmail.com", licenceNumber="LL-956473234"))
# session.add(CarPool(idCar=52, licencePlateNum="01-CC-04"))
# session.commit()

cars = session.query(AllCars).all()
a_cars_list = session.query(CarPool).all()

# for c in cars:
#     print(f'{c.make} - {c.car_id} - {c.model}')
# for cp in a_cars_list:
#     print(cp.idCar, cp.licencePlateNum)
