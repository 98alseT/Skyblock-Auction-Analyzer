import requests
import json

class APIHandler:
    def __init__(self):
        self.API_KEY = None
        try:
            with open('API_KEY.json', 'r') as API_FILE:
                self.API_KEY = json.load(API_FILE)['API_KEY']
        except FileNotFoundError:
            print("Error: Ne postoji file za api")
        except json.JSONDecodeError:
            print("Error: Nije lepo parsiran API key. Moguce da JSON fajl nije dobar.")

    def call(self, url, parms):
        if "auctions" not in url and not self.API_KEY:
            print("Error: Nema API key-a i URL ne sadrzi auctions za koji ne mora API key.")
            return None
        for key, val in parms.items():
            url += f"&{key}={val}"
        return self.__getInfo(url)

    def __getInfo(self, url):
        try:
            r = requests.get(url)
            if r.status_code != 200:
                print(f"Error: Status code {r.status_code} - {r.reason}")
                print(f"Content: {r.text}")
                return None
            return r.json()
        except requests.RequestException as e:
            print(f"Error: Nije uspeo API poziv. Exception: {e}")
            return None

