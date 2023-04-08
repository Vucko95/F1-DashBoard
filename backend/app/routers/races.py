from fastapi import APIRouter
import json, feedparser
from settings.config import *
import requests
from typing import Optional
from datetime import datetime

router = APIRouter()

def get_last_race(races):
    last_race = None
    for race in races:
        if not last_race or race["date"] < last_race["date"]:
            last_race = race
    return last_race


@router.get("/next_race")
async def next_race():
    response = requests.get("https://ergast.com/api/f1/current.json")
    data = response.json()
    races = data["MRData"]["RaceTable"]["Races"]

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
        "url": next_race_data["url"],
        "raceName": next_race_data["raceName"],
        "circuitId": next_race_data["Circuit"]["circuitId"],
        "date": next_race_data["date"],
        "time": next_race_data.get("time")
    }

    return next_race