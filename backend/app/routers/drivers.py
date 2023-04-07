from fastapi import APIRouter
import json
from settings.config import *
import requests
router = APIRouter()




@router.get("/players")
def get_best_players():
    
    
    response = requests.get(url = f1_base_url_plus_drivers_2023)
    f1_base_url_plus_drivers_2023_json = response.json()
    list_of_drivers = f1_base_url_plus_drivers_2023_json['MRData']['DriverTable']['Drivers']
    print(f1_base_url_plus_drivers_2023_json)
    drivers = []
    for driver in list_of_drivers:
        drivers.append({'driverId' : driver['driverId'],'givenName' : driver['givenName'],'familyName' : driver['familyName'],'permanentNumber' : driver['permanentNumber'], })
    print(drivers)
    return drivers


@router.post("/year")
def get_base_player_info(data: dict):
    year = data['year']
    f1_base_url  = 'https://ergast.com/api/f1/'
    f1_drivers_by_year = f'{f1_base_url}{year}/drivers.json'
    response = requests.get(url = f1_drivers_by_year)
    f1_drivers_by_year_json = response.json()
    list_of_drivers = f1_drivers_by_year_json['MRData']['DriverTable']['Drivers']
    # print(f1_drivers_by_year_json)
    drivers = []
    for driver in list_of_drivers:
        drivers.append({'driverId' : driver['driverId'],'givenName' : driver['givenName'],'familyName' : driver['familyName'],'permanentNumber' : driver['permanentNumber'], })
        # drivers.append({'driverId' : driver['driverId']})
    # print(drivers)
    return drivers



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
# @router.post("/year/driverstandings")
# def get_base_player_info(data: dict):
#     year = data['year']
#     f1_base_url  = 'https://ergast.com/api/f1/'
#     f1_drivers_by_year = f'{f1_base_url}{year}/drivers.json'
#     response = requests.get(url = f1_drivers_by_year)
#     f1_drivers_by_year_json = response.json()
#     list_of_drivers = f1_drivers_by_year_json['MRData']['DriverTable']['Drivers']
#     # print(f1_drivers_by_year_json)
#     drivers = []
#     for driver in list_of_drivers:
#         drivers.append({'driverId' : driver['driverId'],'givenName' : driver['givenName'],'familyName' : driver['familyName'],'permanentNumber' : driver['permanentNumber'], })
#     # print(drivers)
#     return drivers


# https://ergast.com/api/f1/2018/constructorStandings
@router.post("/year/driverstandings")
def get_base_player_info(data: dict):
    year = data['year']
    f1_drivers_by_year = f'{f1_base_url}{year}/driverStandings.json'
    response = requests.get(url = f1_drivers_by_year)
    f1_driver_standings_by_year = response.json()
    list_of_drivers = f1_driver_standings_by_year['MRData']["StandingsTable"]["StandingsLists"][0]["DriverStandings"]
    # drivers = []
    drivers = []

    for driver_standing in list_of_drivers:
        driver = driver_standing['Driver']
        driverstats = driver_standing
        constructor_info = driver_standing['Constructors'][0]

        drivers.append({'driverId': driver['driverId'],
                        'constructor_id' : constructor_info['constructorId'],
                        'constructor' : constructor_info['name'],
                        'points' : driverstats['points'],
                        'givenName': driver['givenName'],
                        'familyName': driver['familyName'],
                        'permanentNumber': driver['permanentNumber']})
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