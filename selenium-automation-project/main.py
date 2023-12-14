import random

from selenium.webdriver.common.by import By

gecko_path = r'geckodriver.exe'
from selenium import webdriver
import time
from selenium.webdriver.firefox.service import Service
service = Service(gecko_path)
profile = webdriver.FirefoxProfile()
options = webdriver.FirefoxOptions()
options.profile = profile


PROXY = "45.70.237.132:4145" # HOST: PORT
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f'--proxy-server={PROXY}')

driver = webdriver.Firefox(service=service, options=options)

target_url = "https://in.indeed.com/jobs?q=Data+Scientist&l=Pune"
Job_data = []
for page in range(0, 50, 10):
    driver.get(f"{target_url}&start={page}")
    try:
        close = driver.find_element(By.XPATH, '//button[@class="icl-CloseButton icl-Modal-close"]')
        close.click()
    except:
        pass
    jobs = driver.find_elements(By.XPATH, '//div[@class="css-1m4cuuf e37uo190"]')
    for job in jobs:
        job.location_once_scrolled_into_view
        job.click()
        time.sleep(random.uniform(4.6, 6.9))

driver.quit()


