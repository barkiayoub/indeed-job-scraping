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
chrome_options = webdriver.FirefoxOptions()
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
        """Job_title = driver.find_element(By.XPATH,'/html/body/main/div/div[1]/div/div[5]/div[2]/div/div/div/div/div[1]/div/div[2]/div[1]/h2/span')
        title = Job_title.split('\n')
        Company = driver.find_element(By.XPATH, '//div[@class="css-1cjkto6 eu4oa1w0"]')
        cmpny = Company.split('\n')
        Location = driver.find_element(By.XPATH, '/html/body/main/div/div[1]/div/div[5]/div[2]/div/div/div/div/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div').text.strip()
        loc = Location.split('\n')"""
        span_element = driver.find_element(By.XPATH,'/html/body/main/div/div[1]/div/div[5]/div[2]/div/div/div/div/div[1]/div/div[1]/div[2]/div/div/div/div[1]/div[1]/span')

        # Locate the <a> tag inside the <span>
        anchor_element = span_element.find_element(By.XPATH,'.//a')

        # Get the text of the <a> tag
        anchor_text = anchor_element.text
        print(anchor_text)

driver.quit()


