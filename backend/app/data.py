from sqlalchemy import Integer, create_engine , Column, String, Date, Float, Time


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE_URL = 'mysql+pymysql://root:123@localhost:3306/f1db'
engine = create_engine(DATABASE_URL)
Session  = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()






# def get_drivers_2023():
#     session = Session()
#     drivers = session.query(Driver).all()
#     session.close()

#     drivers_list = []
#     for driver in drivers:
#         drivers_list.append({
#             "id": driver.driverId,
#             "full_name": f"{driver.forename} {driver.surname}",
#             "number": driver.number,
#             "code": driver.code,
#             "nationality": driver.nationality
#         })

#     return drivers_list


# drivers_2023 = get_drivers_2023()
# print(drivers_2023)