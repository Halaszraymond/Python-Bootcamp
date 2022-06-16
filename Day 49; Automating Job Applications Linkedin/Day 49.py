from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

URL = "https://www.linkedin.com/jobs/search/?currentJobId=3120363038&f_AL=true&f_WT=2&geoId=102890719&sortBy=R"
email = "geenideejantje@yahoo.com"
password = "g7$v&Qm#5kDZxH"
phonenumber = "12345678910"

chrome_driver_path = "/bin/chromedriver"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get(URL)


def sign_in(email, password):
    driver.find_element(By.XPATH, '/html/body/div[3]/header/nav/div/a[2]').click()
    driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(email)
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button').click()


def apply(phonenumber):
    driver.find_element(By.XPATH, '//*[@class="jobs-apply-button artdeco-button artdeco-button--3 artdeco-button--primary ember-view"]').click()
    driver.find_element(By.XPATH,
                            '//*[@id="urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:3120363038,60050861,phoneNumber~nationalNumber)"]').send_keys(
            phonenumber)
    driver.find_element(By.XPATH, '//*[@class="artdeco-modal__dismiss artdeco-button artdeco-button--circle artdeco-button--muted artdeco-button--2 artdeco-button--tertiary ember-view"]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@class="artdeco-modal__confirm-dialog-btn artdeco-button artdeco-button--2 artdeco-button--primary ember-view"]').click()


sign_in(email, password)
time.sleep(2)
apply(phonenumber)
time.sleep(5)
driver.quit()