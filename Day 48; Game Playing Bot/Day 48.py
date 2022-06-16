from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "/bin/chromedriver"
ser = Service(chrome_driver_path)
driver = webdriver.Chrome(service=ser)

driver.get("https://www.python.org/")
elements = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul')
elements = elements.text.split("\n")

time = [item for item in elements if elements.index(item) % 2 == 0]
name = [item for item in elements if elements.index(item) % 2 != 0]
mydict = {number: [time[number], name[number]] for number in range(len(time))}
print(mydict)

driver.quit()
