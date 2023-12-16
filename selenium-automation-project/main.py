import csv
import random
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from selenium.webdriver.firefox.service import Service
import pandas as pd

gecko_path = r'C:\\Users\\Asus VivoBook 11TH\\Downloads\\geckodriver.exe'
service = Service(gecko_path)
profile = webdriver.FirefoxProfile()
options = webdriver.FirefoxOptions()
options.profile = profile


PROXY = "103.23.101.97:4145" # HOST: PORT
firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument(f'--proxy-server={PROXY}')

time.sleep(5)
driver = webdriver.Firefox(service=service, options=options)

query = "Software Engineer"
location = "Bangalore"

target_url = f"https://in.indeed.com/jobs?q={query.replace(' ', '+')}&l={location.replace(' ', '+')}"
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
        try:
            close = driver.find_element(By.XPATH, '//button[@class="icl-CloseButton icl-Modal-close"]')
            close.click()
        except:
            pass
        job.location_once_scrolled_into_view
        job.click()
        time.sleep(random.uniform(4.6, 6.9))
        if (driver.find_elements(By.XPATH, '//*[@id="mosaic-desktopserpjapopup"]')):
            outer_div_element = driver.find_element(By.XPATH, '//*[@id="mosaic-desktopserpjapopup"]')
            inner_div_element = outer_div_element.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[1]')
            button_element = inner_div_element.find_element(By.XPATH, ".//button")
            button_element.click()

        #Company name    
        company_span_element = driver.find_element(By.XPATH,"//span[@class='css-1cxc9zk e1wnkr790']")
        company_anchor_element = company_span_element.find_element(By.XPATH, './/a')
        Company = company_anchor_element.text
        print("Company: ",Company)

        #Job
        h2_element = driver.find_element(By.XPATH, "//h2[@class='jobsearch-JobInfoHeader-title css-161nklr e1tiznh50']")
        span_element = h2_element.find_element(By.XPATH, './/span') 
        span_text = span_element.text
        print("Job: ", span_text)

        #Location
        outer_div_element = driver.find_element(By.XPATH, "//div[@class='css-6z8o9s eu4oa1w0']") 
        inner_div_text = outer_div_element.find_element(By.XPATH, './/div')
        inner_div_text = inner_div_text.text
        print("Location: ", inner_div_text)
        
        #Description
        all_div_elements = driver.find_element(By.XPATH, "//div[@class='jobsearch-JobComponent-description css-10ybyod eu4oa1w0']") 
        divs_in_desc = all_div_elements.find_element(By.XPATH, './/div')
        divs_in_desc = divs_in_desc.text
        print("Decription: ", divs_in_desc)
        
        job_data = {
            'Title': span_text,
            'Location': inner_div_text,
            'Company': Company,
            'Decription': divs_in_desc
        }
        Job_data.append(job_data)

        if len(Job_data) == 10:
            driver.quit()
            break



try:
    df = pd.DataFrame(Job_data)
    df.to_excel('C:\\Users\\Asus VivoBook 11TH\\Desktop\\indeedjobs.xlsx')
    print("Excel file saved successfully.")
except Exception as file_error:
    print("An error occurred during Excel file creation:", file_error)
    