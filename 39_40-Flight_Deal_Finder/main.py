#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
# from notification_manager import NotificationManager
from flight_search import FlightSearch

from pprint import pprint
from datetime import datetime, timedelta

ORIGIN_CITY_IATA = "LAX"

data_manager = DataManager()
flight_search = FlightSearch()
# notification_manager = NotificationManager()

sheet_data = data_manager.get_destination_data()

'''Update sheet_data with TESTING in iataCode column'''
if sheet_data[0]["iataCode"] == "":
    city_names = [row["city"] for row in sheet_data]
    print(city_names)
    codes = flight_search.get_destination_code(city_names)
    data_manager.update_destination_codes()
    sheet_data = data_manager.get_destination_data()

'''flights beteen tomorrow and in 6 months'''
today = datetime.now() + timedelta(1)
six_month_from_today = datetime.now() + timedelta(6 * 30)

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=today,
        to_time=six_month_from_today
    )

    # if flight.price < destination["lowestPrice"]:
    #     notification_manager.send_sms(
    #         message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
    #     )
