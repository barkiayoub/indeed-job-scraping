import csv
import random
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from selenium.webdriver.firefox.service import Service

gecko_path = r'geckodriver.exe'
service = Service(gecko_path)
profile = webdriver.FirefoxProfile()
options = webdriver.FirefoxOptions()
options.profile = profile


PROXY = "45.70.237.132:4145" # HOST: PORT
firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument(f'--proxy-server={PROXY}')

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
        if (driver.find_elements(By.XPATH, '//*[@id="mosaic-desktopserpjapopup"]')):
            outer_div_element = driver.find_element(By.XPATH, '//*[@id="mosaic-desktopserpjapopup"]')
            inner_div_element = outer_div_element.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[1]')
            button_element = inner_div_element.find_element(By.XPATH, ".//button")
            button_element.click()

        outer_div_element = driver.find_element(By.XPATH,"//div[@class='css-1cjkto6 eu4oa1w0']")
        company_span_element = outer_div_element.find_element(By.XPATH,'/html/body/main/div/div[1]/div/div[5]/div[2]/div/div/div/div/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div[1]/span')
        company_anchor_element = company_span_element.find_element(By.XPATH, './/a') # Locate the <a> tag inside the <span>
        Company = company_anchor_element.text # Get the text of the <a> tag
        print(Company)

        #div_element = driver.find_element(By.XPATH,'/html/body/main/div/div[1]/div/div[5]/div[2]/div/div/div/div/div[1]/div/div[1]/div[1]')
        div_element = driver.find_element(By.XPATH,'/html/body/main/div/div[1]/div/div[5]/div[2]/div/div/div/div/div[1]/div/div[2]/div[1]')
        h2_element = div_element.find_element(By.XPATH, './/h2')  # Locate the <h2> tag inside the <div>
        span_element = h2_element.find_element(By.XPATH, './/span')  # Locate the <span> tag inside the <h2>
        span_text = span_element.text  # Get the text inside the <span> tag
        print("Job: ", span_text)

        outer_div_element = driver.find_element(By.XPATH, '/html/body/main/div/div[1]/div/div[5]/div[2]/div/div/div/div/div[1]/div/div[1]/div[2]/div/div/div/div[2]')
        inner_div_element = outer_div_element.find_element(By.XPATH, '/html/body/main/div/div[1]/div/div[5]/div[2]/div/div/div/div/div[1]/div/div[1]/div[2]/div/div/div/div[2]/div')  # Locate the inner <div> element inside the outer <div>
        inner_div_text = inner_div_element.text # Get the text inside the inner <div>
        print("Location: ", inner_div_text)
        job_data = {
            'Title': span_text,
            'Location': inner_div_text,
            'Company': Company
        }
        Job_data.append(job_data)


driver.quit()

fields = ['Title', 'Location', 'Company']

with open('jobs.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fields)

    # Write header
    writer.writeheader()

    # Write data
    writer.writerows(Job_data)
