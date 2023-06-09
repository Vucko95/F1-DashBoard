from datetime import datetime
from fastapi import APIRouter
from settings.config import *
import requests

router = APIRouter()


@router.get("/circuits")
def get_circuits(year: str = None):
    if not year:
        year = datetime.now().year
    
    circuits_url = f'https://ergast.com/api/f1/{year}/circuits.json'

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


@router.get("/circuits/{circuit_id}")
def get_circuit_results(circuit_id: str, year: str = None):
    if not year:
        year = datetime.now().year
    
    circuit_results_url = f'https://ergast.com/api/f1/{year}/circuits/{circuit_id}/results.json'

    circuit_results = requests.get(url=circuit_results_url).json()

    race_table = circuit_results['MRData']['RaceTable']['Races']

    race_results = []
    for race in race_table:
        for result in race['Results']:
            race_results.append({
                'raceName': race['raceName'],
                'position': result['position'],
                'driverName': f"{result['Driver']['givenName']} {result['Driver']['familyName']}",
                'points': result['points'],
                'constructor': result['Constructor']['name']
            })

    return race_results

