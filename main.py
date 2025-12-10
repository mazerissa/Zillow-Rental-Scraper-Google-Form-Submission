from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time

ZILLOW_URL = "https://appbrewery.github.io/Zillow-Clone/"
FORMS_URL = "https://forms.gle/k6aois5PdhDe5EG17"


class RentalSearch:
    def __init__(self):
        response = requests.get(ZILLOW_URL)
        self.soup = BeautifulSoup(response.text, "html.parser")

    def get_prices(self):
        return [p.get_text(strip=True) for p in self.soup.select(".PropertyCardWrapper__StyledPriceLine")]

    def get_links(self):
        return [a['href'] for a in self.soup.select(".property-card-link")]

    def get_addresses(self):
        return [p.get_text(strip=True) for p in self.soup.select("address[data-test='property-card-addr']")]


class FormSubmission:
    def __init__(self):
        options = webdriver.FirefoxOptions()
        options.accept_untrusted_certs = True
        self.driver = webdriver.Firefox(options=options)
        self.wait = WebDriverWait(self.driver, 10)  # 10 second wait

    def submit_entry(self, address, price, link):
        self.driver.get(FORMS_URL)

        # Wait for the first input to appear
        address_input = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@role='listitem']//input | //div[@role='listitem']//textarea")
            )
        )

        inputs = self.driver.find_elements(By.XPATH, "//div[@role='listitem']//input | //div[@role='listitem']//textarea")

        if len(inputs) >= 3:
            inputs[0].send_keys(address)
            inputs[1].send_keys(price)
            inputs[2].send_keys(link)
        else:
            print("Could not find all three input fields.")

        # Click submit button
        submit_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div/span/span"))
        )
        submit_button.click()
        time.sleep(2)

# Scrape data
search = RentalSearch()
prices = search.get_prices()
links = search.get_links()
addresses = search.get_addresses()

# Submit each property to the form
form = FormSubmission()
for address, price, link in zip(addresses, prices, links):
    form.submit_entry(address, price, link)


