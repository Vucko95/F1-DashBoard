from datetime import datetime
from fastapi import APIRouter
from pydantic import BaseModel
from settings.config import *
# import aiohttp
import asyncio
import requests
from sqlalchemy.orm import Session
from settings.db import Session
from models.models import *
from fastapi import Depends
router = APIRouter()


# def get_drivers_from_db(year: int, db: Session):
#     return db.query(Driver).filter(Driver.year == year).all()

# def get_driver_standings_from_db(year: int, db: Session):
#     return db.query(DriverStanding, Driver).filter(DriverStanding.year == year).join(Driver, Driver.driverId == DriverStanding.driverId).all()

# def get_driver_standings_from_db(year: int, db: Session):
#     return db.query(DriverStanding, Driver, Constructor).filter(DriverStanding.year == year).join(Driver, Driver.driverId == DriverStanding.driverId).join(Constructor, Constructor.constructorId == DriverStanding.constructorId).all()



# class DriverStandingsRequest(BaseModel):
#     year: int

# @router.get("/drivers")
# def get_best_players(year: str = None, db: Session = Depends(Session)):
#     if not year:
#         year = datetime.now().year

#     drivers = get_drivers_from_db(year, db)

#     drivers_list = []
#     for driver in drivers:
#         drivers_list.append({
#             'driverId': driver.driverId,
#             'givenName': driver.givenName,
#             'familyName': driver.familyName,
#             'permanentNumber': driver.permanentNumber
#         })

#     return drivers_list

# @router.post("/year/driverstandings")
# def get_base_player_info(data: DriverStandingsRequest, db: Session = Depends(Session)):
#     print("Request received:", data)

#     year = data.year

#     driver_standings = get_driver_standings_from_db(year, db)

#     drivers_list = []
#     for driver_standing, driver, constructor in driver_standings:
#         drivers_list.append({
#             'driverId': driver.driverId,
#             'givenName': driver.givenName,
#             'familyName': driver.familyName,
#             'permanentNumber': driver.permanentNumber,
#             'constructor_id': constructor.constructorId,
#             'constructor': constructor.name,
#             'points': driver_standing.points
#         })

#     return drivers_list



# @router.post("/year/driverstandings")
# def get_base_player_info(data: dict):
#     year = data['year']
#     f1_base_url  = 'https://ergast.com/api/f1/'
#     f1_drivers_by_year = f'{f1_base_url}{year}/drivers.json'
#     response = requests.get(url = f1_drivers_by_year)
#     f1_drivers_by_year_json = response.json()
#     list_of_drivers = f1_drivers_by_year_json['MRData']['DriverTable']['Drivers']
#     drivers = []
#     for driver in list_of_drivers:
#         drivers.append({'driverId' : driver['driverId'],'givenName' : driver['givenName'],'familyName' : driver['familyName'],'permanentNumber' : driver['permanentNumber'], })
#     return drivers

# @router.get("/drivers")
# def get_best_players(year: str = None):
#     if not year:
#         year = datetime.now().year

#     drivers_url = f"https://ergast.com/api/f1/{year}/drivers.json"
#     response = requests.get(url = drivers_url).json()

#     list_of_drivers = response['MRData']['DriverTable']['Drivers']

#     drivers = []
#     for driver in list_of_drivers:
#         drivers.append({
#             'driverId' : driver['driverId'],
#             'givenName' : driver['givenName'],
#             'familyName' : driver['familyName'],
#             'permanentNumber' : driver['permanentNumber'] 
#         })

#     return drivers


@router.get("/drivers/{driver_id}")
def get_drivers_results(driver_id: str, year: str = None):
    if not year:
        year = datetime.now().year
    
    driver_url  = f'http://ergast.com/api/f1/{year}/drivers/{driver_id}/results.json'

    races_in_year = requests.get(url = driver_url).json()

    racesList = races_in_year['MRData']['RaceTable']['Races']

    races = []
    for race in racesList:
        races.append({
            'circuitId': race['Circuit']['circuitId'],
            'position' : race['Results'][0]['position'],
            'raceName' : race['raceName'],
            'country' : race['Circuit']['Location']['country'],
        })

    return races


@router.get("/driver-standings")
def get_base_player_info(year: str = None):
    if not year:
        year = datetime.now().year

    driver_standing_url = f'https://ergast.com/api/f1/{year}/driverStandings.json'

    driver_standings = requests.get(url = driver_standing_url).json()

    list_of_drivers = driver_standings['MRData']["StandingsTable"]["StandingsLists"][0]["DriverStandings"]

    drivers = []
    for driver_standing in list_of_drivers:
        driver = driver_standing['Driver']
        constructor_info = driver_standing['Constructors'][0]

        drivers.append({
            'driverId': driver['driverId'],
            'constructor_id' : constructor_info['constructorId'],
            'constructor' : constructor_info['name'],
            'points' : driver_standing['points'],
            'givenName': driver['givenName'],
            'familyName': driver['familyName'],
            'permanentNumber': driver['permanentNumber']
        })

    return drivers





@router.post("/year/constructorstandings")
def get_base_player_info(data: dict):
    year = data['year']
    f1_drivers_by_year = f'{f1_base_url}{year}/constructorStandings.json'
    response = requests.get(url = f1_drivers_by_year)
    constructor_standings  = response.json()
    constructor_standings = constructor_standings ['MRData']['StandingsTable']['StandingsLists'][0]['ConstructorStandings']
    results = []

    for constructor_standing in constructor_standings:
        position = constructor_standing['position']
        name = constructor_standing['Constructor']['name']
        points = constructor_standing['points']
        constructorId = constructor_standing['Constructor']['constructorId']

        results.append({'position': position, 'constructor_id': constructorId, 'name': name, 'points': points})

    # print(results)
    return results

        # constructor_info = driver['Constructors'][0]
        # constructor_info = driver_standing['Constructors']

    #     drivers.append({'driverId': driver['driverId'],
    #                     'constructor_id' : constructor_info['constructorId'],
    #                     'constructor' : constructor_info['name'],
    #                     'points' : driverstats['points'],
    #                     'givenName': driver['givenName'],
    #                     'familyName': driver['familyName'],
    #                     'permanentNumber': driver['permanentNumber']})
    # # print(drivers)
    # return drivers


# @router.get("/driver_points")
# def get_driver_points():
#     return {
#         "drivers": [
#             {
#                 "name": "Max Verstappen",
#                 "points": [0, 12, 25, 38, 54, 64],
#             },
#             {
#                 "name": "Sergio Perez",
#                 "points": [0, 20, 29, 33, 42, 84],
#             },
#         ],
#     }



# @router.post("/driver_points")
# def get_base_player_info(data: dict):
#     year = data['year']
#     drivers_url = f"http://ergast.com/api/f1/{year}/drivers.json"
#     drivers_response = requests.get(drivers_url)
#     drivers_data = drivers_response.json()
#     drivers_list = drivers_data["MRData"]["DriverTable"]["Drivers"]

#     drivers = []
#     for driver in drivers_list:
#         driver_id = driver["driverId"]
#         driver_name = f"{driver['givenName']} {driver['familyName']}"
#         results_url = f"http://ergast.com/api/f1/{year}/drivers/{driver_id}/results.json"
#         results_response = requests.get(results_url)
#         results_data = results_response.json()
#         results_list = results_data["MRData"]["RaceTable"]["Races"]

#         race_points = {"race0": 0}
#         race_number = 1
#         accumulated_points = 0
#         for race in results_list:
#             points = float(race["Results"][0]["points"])
#             accumulated_points += points
#             race_points[f"race{race_number}"] = accumulated_points
#             race_number += 1

#         drivers.append({
#             "driver_name": driver_name,
#             "race_points": race_points
#         })

#     race_labels = ['Season Start'] + [f'Race {i}' for i in range(1, race_number)]
#     return {"year": year, "drivers": drivers, "race_labels": race_labels}
cache = {}

class Year(BaseModel):
    year: int


async def fetch_data(session, url):
    async with session.get(url) as response:
        return await response.json()


async def get_driver_points_async(driver, year):
    driver_id = driver["driverId"]
    driver_name = f"{driver['givenName']} {driver['familyName']}"
    async with aiohttp.ClientSession() as session:
        results_url = f"http://ergast.com/api/f1/{year}/drivers/{driver_id}/results.json"
        results_data = await fetch_data(session, results_url)
        results_list = results_data["MRData"]["RaceTable"]["Races"]

        race_points = {"race0": 0}
        race_number = 1
        accumulated_points = 0
        for race in results_list:
            points = float(race["Results"][0]["points"])
            accumulated_points += points
            race_points[f"race{race_number}"] = accumulated_points
            race_number += 1

        return {
            "driver_name": driver_name,
            "race_points": race_points
        }


@router.post("/driver_points")
async def driver_points(year: Year):
   # CACHE
    if year.year in cache:
        return cache[year.year]

    drivers_url = f"http://ergast.com/api/f1/{year.year}/drivers.json"
    drivers_response = requests.get(drivers_url)
    drivers_data = drivers_response.json()
    drivers_list = drivers_data["MRData"]["DriverTable"]["Drivers"]

    drivers = await asyncio.gather(*[get_driver_points_async(driver, year.year) for driver in drivers_list])


    max_races = max([len(driver["race_points"]) for driver in drivers])


    race_labels = ['Season Start'] + [f'Race {i}' for i in range(1, max_races + 1)]
    result = {"year": year.year, "drivers": drivers, "race_labels": race_labels}

    # CACHE
    cache[year.year] = result
    return result
    
    
    
    
    

# http://ergast.com/api/f1/drivers
@router.get("/test")
def get_best_players():
    test_url = 'http://ergast.com/api/f1/drivers/results.json'
    response = requests.get(url = test_url)
    response_json = response.json()
    print(response_json)
    # list_of_drivers = f1_base_url_plus_drivers_2023_json['MRData']['DriverTable']['Drivers']
    # print(f1_base_url_plus_drivers_2023_json)
    # drivers = []
    # for driver in list_of_drivers:
    #     drivers.append({'driverId' : driver['driverId'],'givenName' : driver['givenName'],'familyName' : driver['familyName'],'permanentNumber' : driver['permanentNumber'], })
    # print(drivers)
    # return drivers

# https://ergast.com/api/f1/2018/driverStandings
