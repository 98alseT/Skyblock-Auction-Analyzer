import re
import consts as const
from APIHandler import APIHandler

class ahItem:
    def __init__(self, items):
        items = self.__cleanUp(items)
        for key, val in items.items():
            if key in const.ignore: 
                continue
            setattr(self, key, val)

        setattr(self, "level", None)
        setattr(self, "reforge", None)

    def __cleanUp(self, items):
        items["item_name"] = re.sub(r'[^\x00-\x7F]+', '', items["item_name"])
        items["item_name"] = self.__translateLevel(items["item_name"])
        items["item_name"] = self.__translateReforge(items["item_name"], items["category"])
        items["item_name"] = items["item_name"].lstrip()
        items["item_name"] = items["item_name"].rstrip()
        return items

    def __translateReforge(self, name, category):
        if category not in const.reforges:
            return name
        
        try:
            potential_reforge, new_name = name.split(maxsplit=1)
            if potential_reforge in const.reforges[category]:
                self.reforge = potential_reforge
                return new_name
            return name
        except ValueError:
            return name

    def __translateLevel(self, name):
        if name[0] == '[':
            i = name.find(']')
            try:
                self.level = int(name[5:i].strip())
            except ValueError:
                self.level = None
            name = name[i+1:].strip()
        return name

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