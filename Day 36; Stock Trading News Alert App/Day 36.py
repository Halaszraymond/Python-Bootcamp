import requests
from datetime import datetime
from datetime import timedelta
from twilio.rest import Client

current_day = datetime.today()
day_before_this_one = current_day - timedelta(days=1)
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
alphavantage_api_key = "{ALPHAVANTAGE_API_KEY}"
news_api_key = "{NEWS_API_KEY}"
twilio_account_sid = "{TWILIO_ACCOUNT_SID}"
twilio_auth_token = "{TWILIO_AUTH_TOKEN}"
today_weekend = False
yesterday_weekend = False


def today(this_day):
    today_year = this_day.year
    today_month = this_day.month
    today_day = this_day.day
    if this_day.weekday() == 5:
        today_day -= 1
    elif this_day.weekday() == 6:
        today_day -= 2
    formatted_today = f"{today_year}-0{today_month}-0{today_day}"
    return formatted_today


def yesterday(one_day_ago):
    yesterday_year = one_day_ago.year
    yesterday_month = one_day_ago.month
    yesterday_day = one_day_ago.day
    if one_day_ago.weekday() == 5:
        yesterday_day -= 1
    elif one_day_ago.weekday() == 6:
        yesterday_day -= 2
    formatted_yesterday = f"{yesterday_year}-0{yesterday_month}-0{yesterday_day}"
    return formatted_yesterday


parameters_alphavantage = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": STOCK,
    "interval": "60min",
    "apikey": alphavantage_api_key,
}

parameters_news = {
    "qInTitle": COMPANY_NAME,
    "apiKey": news_api_key,
}

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_response = requests.get("https://www.alphavantage.co/query", params=parameters_alphavantage)
stock_data = stock_response.json()

closing = float(stock_data["Time Series (60min)"][f"{today(current_day)} 20:00:00"]["4. close"])
opening = float(stock_data["Time Series (60min)"][f"{yesterday(day_before_this_one)} 05:00:00"]["1. open"])

perc_difference = (closing / opening * 100) - 100

if perc_difference > 5 or perc_difference < 5:
    ## STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    news_response = requests.get("https://newsapi.org/v2/everything", params=parameters_news)
    news_articles = news_response.json()["articles"]
    three_articles = news_articles[:3]
    for article in three_articles:
        ## STEP 3: Use https://www.twilio.com
        # Send a seperate message with the percentage change and each article's title and description to your phone number.
        headline = article["title"]
        description = article["description"]
        client = Client(twilio_account_sid, twilio_auth_token)
        message = client.messages \
            .create(
            body=f"TSLA: {round(perc_difference)}\n"
                 f"Headline: {headline}\n"
                 f"Brief: {description}",
            from_="+19784806248",
            to="{YOUR_PHONE_NUMBER}"
        )

# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
