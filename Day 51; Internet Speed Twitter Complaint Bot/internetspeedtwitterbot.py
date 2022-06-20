from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

promised_dow = 150
promised_up = 18
chrome_driver_path = "/bin/chromedriver"
twitter_mail = "halaszraymond@gmail.com"
twitter_password = "twitter_password"
service = Service(chrome_driver_path)
URL_SPEEDTEST = "https://www.speedtest.net/"
URL_TWITTER = "https://twitter.com/"


class InternetSpeedTwitterBot:

    def __init__(self):
        self.driver = webdriver.Chrome(service=service)
        self.normal_down = 120
        self.normal_up = 150
        self.down = 0
        self.up = 0
        self.tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {self.normal_down}down/{self.normal_up}up?"

    def get_internet_speed(self):
        self.driver.get(URL_SPEEDTEST)
        self.driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a').click()
        time.sleep(45)
        self.down = float(self.driver.find_element(By.XPATH,
                                                   '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                                   '3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)
        self.up = float(self.driver.find_element(By.XPATH,
                                                 '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                                 '3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text)
        dict = {"download": self.down, "upload": self.up}
        return dict

    def tweet_at_provider(self):
        self.driver.get(URL_TWITTER)
        self.driver.find_element(By.XPATH,
                                 '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a').click()
        self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div['
                                           '2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input').send_keys({
            "email/userame/phonenumber"})
        self.driver.find_element(By.XPATH,
                                 '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div['
                                 '2]/div/div/div/div[6]').click()
        self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div['
                                           '2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div['
                                           '1]/input').send_keys({"password"})
        self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div['
                                           '2]/div[2]/div[2]/div/div[1]/div/div/div').click()
        try:
            self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div['
                                               '2]/div/div/div/div/div[2]/div[2]').click()
        except:
            pass
        if self.normal_down > self.down or self.normal_up > self.up:
            self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div['
                                               '2]/div/div[2]/div[1]/div/div/div/div[2]/div['
                                               '1]/div/div/div/div/div/div/div/div/div/label/div['
                                               '1]/div/div/div/div/div[2]/div/div/div/div').send_keys(self.tweet)
            self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div['
                                               '2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div['
                                               '3]').click()
            print("Tweet Sent")
        else:
            print("It was not necessary to send a tweet, have a great day")
