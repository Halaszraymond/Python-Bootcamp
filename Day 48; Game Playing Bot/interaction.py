from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "/bin/chromedriver"
ser = Service(chrome_driver_path)
driver = webdriver.Chrome(service=ser)
# timeout = time.time() + 300
iterations = 1
cookie_click = True

driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.XPATH, '//*[@id="cookie"]')
upgrades = ["BuyTime machine", "buyPortal", "buyAlchemy lab", "buyShipment", "buyMine", "buyFactory", "buyGrandma",
            "buyCursor"]


while cookie_click:
    for _ in range(iterations):
        cookie.click()
    for upgrade in upgrades:
        try:
            driver.find_element(By.ID, upgrade).click()
        except:
            continue
    iterations += 10

cps = driver.find_element(By.ID, "cps")
print(cps.text)
driver.quit()

