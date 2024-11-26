#Imports
import requests
import json
import os
import shutil
from APIHandler import APIHandler
from Ah import AuctionHouse

#Functions
def deleteTemp():
    try:
        shutil.rmtree("temp")
    except: pass

def jsonWrite(file, content):
    os.makedirs("temp", exist_ok=True)
    with open("temp/"+file,'w') as f:
        json.dump(content, f, indent=4)

#Variables
API_FILE = open("API_KEY.json", "r")
API_KEY = json.loads(API_FILE.read())['API_KEY']
UUID = None
playerName = None
playerQuery = f"https://api.hypixel.net/v2/player?key={API_KEY}&name={playerName}"
auctionQuery = f"https://api.hypixel.net/v2/skyblock/auctions?"
uuidToPlayerQuery = f"https://sessionserver.mojang.com/session/minecraft/profile/{UUID}"
client = APIHandler()
ahList = []

#Code
deleteTemp()
scrapeAuctionHouse()
print(len(ahList))
