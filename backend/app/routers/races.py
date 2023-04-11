from fastapi import APIRouter
from settings.config import *
import requests
from datetime import datetime

router = APIRouter()

def get_last_race(races):
    last_race = None
    for race in races:
        if not last_race or race["date"] < last_race["date"]:
            last_race = race
    return last_race


@router.get("/next-race")
async def next_race():
    current_race_url = "https://ergast.com/api/f1/current.json"
    
    response = requests.get(current_race_url).json()

    races = response["MRData"]["RaceTable"]["Races"]

    current_date = datetime.now().date()
    next_race_data = None

    for race in races:
        race_date = datetime.strptime(race["date"], "%Y-%m-%d").date()
        if race_date > current_date:
            next_race_data = race
            break

    if not next_race_data:
        return {"error": "No more races this season"}

    next_race = {
        "season": next_race_data["season"],
        "round": next_race_data["round"],
        "country": races[0]["Circuit"]["Location"]['country'],
        "url": next_race_data["url"],
        "raceName": next_race_data["raceName"],
        "circuitId": next_race_data["Circuit"]["circuitId"],
        "first_practice_date": next_race_data['FirstPractice']['date'],
        "race_date": next_race_data["date"],
        "date": next_race_data["date"],
        "time": next_race_data.get("time"),

        # START TIMES
        "startFP1": next_race_data['FirstPractice']['time'],
        "startFP2": next_race_data['SecondPractice']['time'],
        "startQualy": next_race_data['Qualifying']['time'],
        "startSprint": next_race_data['Sprint']['time'],
        "startRace": next_race_data['time'],
    }

    return next_race




@router.get("/past-race")
async def previous_race():
    response = requests.get("https://ergast.com/api/f1/current.json")
    data = response.json()
    races = data["MRData"]["RaceTable"]["Races"]

    current_date = datetime.now().date()
    previous_race_data = None

    for race in reversed(races):
        race_date = datetime.strptime(race["date"], "%Y-%m-%d").date()
        if race_date < current_date:
            previous_race_data = race
            break

    if not previous_race_data:
        return {"error": "No previous races this season"}
    previous_race = {
        "season": previous_race_data["season"],
        "round": previous_race_data["round"],
        "country": previous_race_data["Circuit"]["Location"]['country'],
        "url": previous_race_data["url"],
        "raceName": previous_race_data["raceName"],
        "circuitId": previous_race_data["Circuit"]["circuitId"],
        "first_practice_date": previous_race_data['FirstPractice']['date'],
        "race_date": previous_race_data["date"],
        "date": previous_race_data["date"],
        "time": previous_race_data.get("time"),
        # START TIMES
        "startFP1": previous_race_data['FirstPractice']['time'],
        "startFP2": previous_race_data['SecondPractice']['time'],
        "startQualy": previous_race_data['Qualifying']['time'],
        # MOST RACES DONT HAVE SPRINT
        "startSprint": previous_race_data.get('Sprint', {}).get('time', None),
        "startRace": previous_race_data['time'],
    }

    return previous_race


@router.get("/top-drivers")
async def get_top_drivers(year: str = None):
    if not year:
        year = datetime.now().year
        
    top_drivers_url = f"https://ergast.com/api/f1/{year}/last/results.json"

    top_drivers = requests.get(top_drivers_url).json()

    previous_race_data = top_drivers["MRData"]["RaceTable"]["Races"][0]

    round_number = previous_race_data["round"]

    results_response = requests.get(f"http://ergast.com/api/f1/{year}/{round_number}/results.json")

    results_data = results_response.json()["MRData"]["RaceTable"]["Races"][0]["Results"]

    top_drivers = []
    for result in results_data:
        top_drivers.append({
            'driver_name' : result['Driver']['givenName'],
            'driver_surname' : result['Driver']['familyName'],
            # SOME DRIVERS DONT HAVE TIME
            'driver_time': result.get('Time', {}).get('time', None),
            'driver_points' : result['points'],
        })

    top_three_drivers = top_drivers[:3]

    return top_three_drivers
