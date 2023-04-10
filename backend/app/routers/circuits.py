from datetime import datetime
from fastapi import APIRouter
from pydantic import BaseModel
from settings.config import *
import requests

router = APIRouter()


class CircuitBody(BaseModel):
    year: int

@router.get("/circuits")
def get_circuits(body: CircuitBody):
    circuits_url = f'https://ergast.com/api/f1/{body.year}/circuits.json'

    circuits_by_year = requests.get(url = circuits_url).json()

    circuits_list = circuits_by_year['MRData']['CircuitTable']['Circuits']

    circuits = []
    for circuit in circuits_list:
        circuits.append({
            'circuitId': circuit['circuitId'],
            'circuitName' : circuit['circuitName'],
            'country' : circuit['Location']['country'],
        })

    return circuits


class CircuitDriverBody(BaseModel):
    year: int
    driver_id: str

@router.get("/circuits/driver")
def get_circuit_drivers(body: CircuitDriverBody):
    driver_url  = f'http://ergast.com/api/f1/{body.year}/drivers/{body.driver_id}/results.json'

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


class CircuitResultsBody(BaseModel):
    year: int
    circuit_id: str

@router.get("/circuit_results")
def get_circuit_results(body: CircuitResultsBody):
    circuit_results_url = f'https://ergast.com/api/f1/{body.year}/circuits/{body.circuit_id}/results.json'

    circuit_results = requests.get(url=circuit_results_url).json()

    race_table = circuit_results['MRData']['RaceTable']['Races']

    race_results = []
    for race in race_table:
        for result in race['Results']:
            race_results.append({
                'raceName': race['raceName'],
                'position': result['position'],
                'driverName': f"{result['Driver']['givenName']} {result['Driver']['familyName']}",
                'constructor': result['Constructor']['name']
            })

    return race_results


class CircuitYearBody(BaseModel):
    year: int

@router.post("/circuits/year")
def get_circuits_by_year(body: dict):
    circuits_in_year_url = f'https://ergast.com/api/f1/{body.year}/circuits.json'
    circuits_in_year_response = requests.get(url=circuits_in_year_url).json()
   
    circuit_list = circuits_in_year_response['MRData']['CircuitTable']['Circuits']

    circuits = []
    for circuit in circuit_list:
        circuits.append({
            'circuitId': circuit['circuitId'],
            'circuitName': circuit['circuitName'],
            'country': circuit['Location']['country'],
        })

    return circuits


class CircuitResultsBody(BaseModel):
    year: int
    circuit_id: str

@router.get("/circuits/track/result")
def get_circuit_results(body: CircuitResultsBody):
    circuit_results_url = f'http://ergast.com/api/f1/{body.year}/circuits/{body.circuit_id}/results.json'

    circuit_results = requests.get(url=circuit_results_url).json()

    race_list = circuit_results['MRData']['RaceTable']['Races']

    results = []
    for race in race_list:
        for result in race['Results']:
            results.append({
                'driverName': f"{result['Driver']['givenName']} {result['Driver']['familyName']}",
                'position': result['position'],
                'points': result['points'],
            })

    return results