from githubUserInfo import arama
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

s = Service(r"C:\Program Files (x86)\chromedriver.exe")

class Github:
    def __init__(self, arama):
        self.browser = webdriver.Chrome(service=s)
        self.arama = arama
        
    def signIn(self):
        self.browser.get("https://github.com/")
        time.sleep(2)
        ara = self.browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/header/div/div[2]/div/div/qbsearch-input/div[1]/button/span")
        ara.click
        ara.send_keys(Keys, self.arama)
        
    

