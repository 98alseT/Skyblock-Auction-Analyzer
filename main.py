#Imports
import os
import shutil
import json
from Ah import AuctionHouse
from collections import defaultdict

#Functions
def deleteTemp():
    try:
        shutil.rmtree("temp")
    except: pass

def jsonWrite(file, content):
    os.makedirs("temp", exist_ok=True)
    with open("temp/"+file+".json",'w') as f:
        json.dump(content, f, indent=2)

#Variables
auctions = AuctionHouse()

#Code
deleteTemp()
auctions.scrape()
print(auctions.size())

svi_nazivi_itema = defaultdict(lambda: defaultdict(dict))

for i in auctions.list_of_items:
    svi_nazivi_itema[i["category"]][i["item_name"]] = True

for key, val in svi_nazivi_itema.items():
    jsonWrite(key, val)
