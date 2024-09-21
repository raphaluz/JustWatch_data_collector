import os
import time
from webdriver_manager.chrome import ChromeDriverManager 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Scraper:
    def __init__(self):
        self.setup_driver()

    def setup_driver(self):
        chrome_options = Options()
        #chrome_options.add_argument("--headless")  # Run in headless mode
        
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=chrome_options)

    def scrape_website(self, url):
        self.driver.get(url)
        # Add your scraping logic here
        pass

    def close(self):
        self.driver.quit()