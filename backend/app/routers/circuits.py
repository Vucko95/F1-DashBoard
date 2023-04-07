from fastapi import APIRouter
import json
from settings.config import *
import requests
router = APIRouter()



# @router.get("/circuits")
# def get_base_player_info():
@router.post("/circuits")
def get_base_player_info(data: dict):
    year = data['year']
    # year = 2022
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


