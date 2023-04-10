from fastapi import APIRouter
import json
from settings.config import *
import requests
from datetime import datetime

router = APIRouter()



# @router.get("/circuits")
# def get_base_player_info():
@router.post("/circuits")
def get_base_player_info(data: dict):
    year = data['year']
    # year = 2022
    f1_base_url  = 'https://ergast.com/api/f1/'

    circuitsInYear = f'{f1_base_url}{year}/circuits.json'
    circuitsInYear = requests.get(url = circuitsInYear)
    circuitsInYear_json = circuitsInYear.json()
    circuitList = circuitsInYear_json['MRData']['CircuitTable']['Circuits']
    circuits = []
    for circuit in circuitList:
        circuitId = circuit['circuitId']
        circuitName = circuit['circuitName']
        country = circuit['Location']['country']
        circuits.append({
                'circuitId': circuitId,
                'circuitName' : circuitName,
                'country' : country,
                })
    # print(circuits)
    # print(circuits)
    return circuits



@router.post("/circuits/driver")
def get_base_player_info(data: dict):
    year = data['year']
    driverID = data['driverID']
    # hardcoded_driver_url  = 'http://ergast.com/api/f1/2021/drivers/hamilton/results.json'
    dirver_url  = f'http://ergast.com/api/f1/{year}/drivers/{driverID}/results.json'

    # circuitsInYear = f'{f1_base_url}{year}/circuits.json'
    racesInYear = requests.get(url = dirver_url)
    racesInYear_json = racesInYear.json()
    # circuitList = circuitsInYear_json['MRData']['CircuitTable']['Circuits']
    racesList = racesInYear_json['MRData']['RaceTable']['Races']
    races = []
    for race in racesList:
        circuitId = race['Circuit']['circuitId']
        position =race['Results'][0]['position']
        raceName =race['raceName']
        country = race['Circuit']['Location']['country']
        races.append({
                'circuitId': circuitId,
                'position' : position,
                'raceName' : raceName,
                'country' : country,
                })
    print(races)
    # print(circuits)
    return races



@router.post("/circuit_results")
def get_circuit_results(data: dict):
    year = data['year']
    circuit_id = data['circuit_id']

    f1_base_url  = 'https://ergast.com/api/f1/'

    results_url = f'{f1_base_url}{year}/circuits/{circuit_id}/results.json'
    results_response = requests.get(url=results_url)
    results_json = results_response.json()

    race_table = results_json['MRData']['RaceTable']['Races']

    race_results = []

    for race in race_table:
        race_name = race['raceName']
        results = race['Results']
        for result in results:
            position = result['position']
            driver = result['Driver']
            driver_name = f"{driver['givenName']} {driver['familyName']}"
            constructor = result['Constructor']['name']
            race_results.append({
                'raceName': race_name,
                'position': position,
                'driverName': driver_name,
                'constructor': constructor
            })

    return race_results


@router.post("/circuits/year")
def get_circuits_by_year(data: dict):
    year = data['year']

    circuits_in_year_url = f'{f1_base_url}{year}/circuits.json'
    circuits_in_year_response = requests.get(url=circuits_in_year_url)
    circuits_in_year_json = circuits_in_year_response.json()
    circuit_list = circuits_in_year_json['MRData']['CircuitTable']['Circuits']

    circuits = []
    for circuit in circuit_list:
        circuit_id = circuit['circuitId']
        circuit_name = circuit['circuitName']
        country = circuit['Location']['country']
        circuits.append({
            'circuitId': circuit_id,
            'circuitName': circuit_name,
            'country': country,
        })

    return circuits



# @router.post("/circuits/track")
# def get_base_player_info(data: dict):
#     year = data['year']
#     driverID = data['driverID']
#     # hardcoded_driver_url  = 'http://ergast.com/api/f1/2021/drivers/hamilton/results.json'
#     dirver_url  = f'http://ergast.com/api/f1/{year}/drivers/{driverID}/results.json'

#     racesInYear = requests.get(url = dirver_url)
#     racesInYear_json = racesInYear.json()
#     # circuitList = circuitsInYear_json['MRData']['CircuitTable']['Circuits']
#     racesList = racesInYear_json['MRData']['RaceTable']['Races']
#     races = []
#     for race in racesList:
#         circuitId = race['Circuit']['circuitId']
#         position =race['Results'][0]['position']
#         raceName =race['raceName']
#         country = race['Circuit']['Location']['country']
#         races.append({
#                 'circuitId': circuitId,
#                 'position' : position,
#                 'raceName' : raceName,
#                 'country' : country,
#                 })
#     print(races)
#     # print(circuits)
#     return races



@router.post("/circuits/track/result")
def get_circuit_results(data: dict):
    year = data['year']
    circuitId = data['circuitId']
    circuit_results_url = f'http://ergast.com/api/f1/{year}/circuits/{circuitId}/results.json'

    circuit_results = requests.get(url=circuit_results_url)
    circuit_results_json = circuit_results.json()
    race_list = circuit_results_json['MRData']['RaceTable']['Races']

    results = []
    for race in race_list:
        for result in race['Results']:
            driver_name = result['Driver']['givenName'] + ' ' + result['Driver']['familyName']
            position = result['position']
            points = result['points']
            results.append({
                'driverName': driver_name,
                'position': position,
                'points': points,
            })
    return results



# @router.get("/ttt")

# def get_next_race(year):
#     # year = 2023
#     url = f'http://ergast.com/api/f1/{year}.json'
#     response = requests.get(url)
#     data = response.json()
#     races = data['MRData']['RaceTable']['Races']

#     current_date = datetime.now().date()

#     for race in races:
#         race_date = datetime.strptime(race['date'], '%Y-%m-%d').date()
#         if race_date >= current_date:
#             return race

#     return None

# current_year = datetime.now().year
# next_race = get_next_race(current_year)
# print(next_race)


