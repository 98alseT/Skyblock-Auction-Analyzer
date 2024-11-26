from APIHandler import APIHandler

class ahItem:
    ignore = [
        "bids",
        "claimed_bidders",
        "highest_bid_ammount",
        "last_updated"
    ]

    def __init__(self, items):
        for key, val in items.items():
            if key in self.ignore: 
                continue
            setattr(self, key, val)

    #python getter i setter
    def __getitem__(self, key): return getattr(self, key, None)
    def __setitem__(self, key, val): setattr(self, key, val)

'''
def scrapeAuctionHouse():
    query = client.call(auctionQuery, {"page" : 0})

    for j in range( len(query["auctions"])):
        if query["auctions"][j]["bin"] == True:
            ahList.append(ahItem(query["auctions"][j]))
    
    velicina = query["totalPages"]
    jsonWrite("ah0.json", query)
    for i in range(1, velicina):
        query = client.call(auctionQuery, {"page" : i})

        for j in range( len(query["auctions"])):
            if query["auctions"][j]["bin"] == True:
                ahList.append(ahItem(query["auctions"][j]))

        if query is None:
            print(f"DID NOT manage to get query {i}")
        else: print(f"Got query {i}")
        jsonWrite(f"ah{i}.json", query)
'''

class AuctionHouse:
    def __init__():
        