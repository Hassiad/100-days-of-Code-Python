
import requests

# https://docs.google.com/spreadsheets/d/1T70yxyBZNw8i4cIFn3T2KGQW1EclIqWmvCSO2s-T-4Y/edit#gid=0
SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/1da9576c220c6df09ab7cf61d9926a2d/flightDeals/prices"

class DataManager:
    def __init__(self):
        self.destination_data = {}
    
    def get_destination_data(self):
        '''Return travel destination data in json format'''
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        self.destination_data = response.json()["prices"]
        return self.destination_data
    
    def update_destination_codes(self):
        '''Update sheets with IATA codes'''
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)   

    