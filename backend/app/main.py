from fastapi import FastAPI
from routers import drivers, circuits, news, races
from fastapi.middleware.cors import CORSMiddleware
import feedparser, json

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(drivers.router)
app.include_router(circuits.router)
app.include_router(news.router)
app.include_router(races.router)


# url = "https://feeds.bbci.co.uk/sport/formula1/rss.xml"
# feed = feedparser.parse(url)
# # with open('feed.json', 'w') as outfile:
# #     json.dump(feed, outfile, ensure_ascii=False, indent=4)
# print("Feed Title:", feed.feed.title)
# print("Feed Link:", feed.feed.link)
# print("Number of Entries:", len(feed.entries))
# news_feed = []
# for entry in feed['entries']:
#     news_feed.append({'articleTitle' :entry.title,'articleSummary' :entry.summary,'articleLink' :entry.link  })
#         # drivers.append({'driverId' : driver['driverId'],'givenName' : driver['givenName'],'familyName' : driver['familyName'],'permanentNumber' : driver['permanentNumber'], })
# print(news_feed)
