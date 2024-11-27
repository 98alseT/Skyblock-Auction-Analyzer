#Imports
import os
import shutil
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
auctions = AuctionHouse()

#Code
auctions.scrape()
print(auctions.size())
