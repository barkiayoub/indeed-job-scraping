import pandas as pd
import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set the path to the GeckoDriver executable
GECKO_PATH = r'geckodriver.exe'

# Create the Firefox driver
driver = webdriver.Firefox(executable_path=GECKO_PATH)

Job_data = []

for page in range(0, 50, 10):
    driver.get(f'https://in.indeed.com/jobs?q=Data+Scientist&l=Pune&start={page}')
    # time.sleep(random.uniform(8.5, 10.9))

# Rest of your code...
