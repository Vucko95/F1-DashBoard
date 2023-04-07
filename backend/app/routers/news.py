from fastapi import APIRouter
import json, feedparser
from settings.config import *
import requests
router = APIRouter()




@router.get("/news")
def get_best_players():
    url = "https://feeds.bbci.co.uk/sport/formula1/rss.xml"
    feed = feedparser.parse(url)

    news_feed = []
    # for entry in feed['entries']:
    # LIMIT 8
    for entry in feed['entries'][:6]:
        news_feed.append({'articleTitle' :entry.title,'articleSummary' :entry.summary,'articleLink' :entry.link,'articlepublished' :entry.published  })
            # drivers.append({'driverId' : driver['driverId'],'givenName' : driver['givenName'],'familyName'published : driver['familyName'],'permanentNumber' : driver['permanentNumber'], })
    print(news_feed)
    return news_feed