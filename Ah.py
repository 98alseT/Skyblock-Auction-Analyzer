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


class AuctionHouse:
    def __init__(self):
        self.list_of_items = []
        self.parms = {"page" : 0}
        self.client = APIHandler()
        self.url = "https://api.hypixel.net/v2/skyblock/auctions?"
    
    def scrape(self):
        self.parms["page"] = 0
        pages = self.__get_Pages()
        for i in range(pages):
            self.parms["page"] = i
            r = self.client.call(self.url, self.parms)
            self.__add_to_list(r["auctions"])
    
    def size(self): return len(self.list_of_items)

    def __add_to_list(self, auctions):
        for i in auctions:
            if self.__check_bin(i):
                self.list_of_items.append(ahItem(i))

    def __check_bin(self, query):
        return query["bin"]

    def __get_Pages(self):
        return self.client.call(self.url)["totalPages"]
        
    def archive(self):
        #dodati kasnije da arhivira svaki put
        pass