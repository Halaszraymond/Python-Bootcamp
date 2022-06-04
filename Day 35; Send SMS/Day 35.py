import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = {"OWM_API_KEY"}
account_sid = "AC09a26062f8573863cc0fb7ec5800f409"
auth_token = {"TWILIO_AUTH_TOKEN"}

parameters = {
    "lat": "MY_LAT",
    "lon": "MY_LONG",
    "exclude": "current,minutely,daily",
    "appid": api_key,
}

response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
rain = False

list_weather_id = [weather_data["hourly"][hour]["weather"][0]["id"] for hour in range(0, 12)]

for weather_id in list_weather_id:
    if weather_id < 700:
        rain = True

if rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body="It's going to rain today! remember to bring an umbrella.",
        from_="+19784806248",
        to="{MY_PHONE_NUMBER}"
    )
    print(message.status)
