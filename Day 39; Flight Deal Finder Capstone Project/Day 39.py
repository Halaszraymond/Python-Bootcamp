from flight_search import FlightSearch
from notification_manager import NotificationManager

sheet_data = FlightSearch().get_dataframe()


for _, row in sheet_data.iterrows():
    city = row["City"]
    price = row["Lowest Price"]
    iata = FlightSearch().iata_code(city)
    flight = FlightSearch().find_price(iata, price, city)
    if flight and flight.price < row["Lowest Price"]:
        message = f"Low price alert! Only {flight.price} EU to fly from {flight.origin_city}-"\
                f"{flight.origin_airport} to"\
                f"{flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to "\
                f"{flight.return_date}."
        message_2 = f"Subject: {message}\n\n" \
                    f"{message}\n" \
                    f"https://www.google.co.uk/flights?hl=en#flt={flight.origin_airport}.{flight.destination_airport}" \
                    f".{flight.out_date}*{flight.destination_airport}.{flight.origin_airport}.{flight.return_date}"\
            .encode("UTF-8")
        if flight.stop_overs > 0:
            message += f"\nFlight has 1 stop over, via {flight.via_city}"
            message_2 += f"\nFlight has 1 stop over, via {flight.via_city}"
        NotificationManager().send_message(message)
        NotificationManager().send_email(message_2)



