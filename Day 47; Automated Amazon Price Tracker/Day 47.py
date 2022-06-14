from bs4 import BeautifulSoup
import requests
import smtplib

URL = "https://www.amazon.nl/Turtle-Beach-Recon-Controller-Zwart/dp/B0977MTK65/ref=sr_1_4?__mk_nl_NL=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=xbox+series+x+controller+bluetooth&qid=1655207011&s=videogames&sr=1-4"
HEADERS = {
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36",

}

response = requests.get(URL, headers=HEADERS)
soup = BeautifulSoup(response.text, "lxml")
price = soup.find(class_="a-offscreen").getText()
price_without_currency = price.split("€")[1]
price_without_currency = price_without_currency.replace(",", ".")
float_price = float(price_without_currency)

if float_price < 40:
    my_email = f"{You_Email}"
    password = f"{Your_Password}"
    with smtplib.SMTP("smtp.mail.yahoo.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="{Receiver_Email}",
                            msg=f"Subject:Amazon Price Alert!!\n\nTurtle Beach Recon Controller Zwart - Xbox Series X|S en Xbox One on Low Price!!\n "
                                f"Now only {float_price}EU!\n"
                                f"{URL}"
                            )
