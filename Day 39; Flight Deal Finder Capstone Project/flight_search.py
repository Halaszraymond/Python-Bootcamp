import requests
from flight_data import FlightData
import pandas as pd
from datetime import datetime
from datetime import timedelta
from pprint import pprint

apikey = "{TEQUILA_API_KEY}"
TEQUILA_KIWI_ENDPOINT = f"https://tequila-api.kiwi.com"
today = datetime.now().strftime("%d/%m/%Y")
six_months = (datetime.now() + timedelta(6 * 30)).strftime("%d/%m/%Y")


class FlightSearch:

    def get_dataframe(self):
        return pd.read_csv("Flight Deals Python.csv")

    def iata_code(self, city_name):
        header = {
            "apikey": apikey,
        }
        kiwi_params = {
            "term": city_name,
            "location_types": "city",
        }
        response = requests.get(url=f"{TEQUILA_KIWI_ENDPOINT}/locations/query", params=kiwi_params, headers=header)
        data = response.json()
        iatacode = data["locations"][0]["code"]
        return iatacode

    def find_price(self, iata, price, city_name):
        header = {
            "apikey": apikey,
        }
        kiwi_params = {
            "fly_from": "AMS",
            "fly_to": iata,
            "date_from": today,
            "date_to": six_months,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "adults": 1,
            "curr": "EUR",
            "price_to": price,
            "limit": 10
        }
        response = requests.get(url=f"{TEQUILA_KIWI_ENDPOINT}/v2/search", params=kiwi_params, headers=header)
        try:
            data = response.json()["data"][0]
        except IndexError:
            try:
                kiwi_params["max_stopovers"] = 1
                response = requests.get(url=f"{TEQUILA_KIWI_ENDPOINT}/v2/search", params=kiwi_params, headers=header)
                data = response.json()["data"][0]
                pprint(data)
                flight_data = FlightData(
                    price=data["price"],
                    origin_city=data["route"][0]["cityFrom"],
                    origin_airport=data["route"][0]["flyTo"],
                    destination_city=data["route"][1]["cityTo"],
                    destination_airport=data["route"][0]["flyTo"],
                    out_date=data["route"][0]["local_departure"].split("T")[0],
                    return_date=data["route"][1]["local_departure"].split("T")[0],
                    stop_overs=1,
                    via_city=data["route"][0]["cityTo"]
                )
                print(f"{flight_data.destination_city}: €{flight_data.price}")
                return flight_data
            except IndexError:
                print(f"No flights found for {city_name}.")
                return None
        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyTo"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0],
            )
            print(f"{flight_data.destination_city}: €{flight_data.price}")
            return flight_data

