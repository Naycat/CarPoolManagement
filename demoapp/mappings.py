from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.automap import automap_base
engine = create_engine("mysql+pymysql://app:appass@127.0.0.1:3306/carPoolDB")

# produce our own MetaData object
metadata = MetaData()

# we can reflect it ourselves from a database, using options
# such as 'only' to limit what tables we look at...
metadata.reflect(bind=engine)

# ... or just define our own Table objects with it (or combine both)

# we can then produce a set of mappings from this MetaData.
Base = automap_base(metadata=metadata)

# calling prepare() just sets up mapped classes and relationships.
Base.prepare()

# mapped classes are ready
AllCars = Base.classes.allCarOptions
CarPool = Base.classes.carPool
Booking = Base.classes.reservations
Drivers = Base.classes.drivers
