from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
kişi = input("Aramak istediğiniz kişiyi giriniz : ")
s = Service(r"C:\Program Files (x86)\chromedriver.exe")
browser = webdriver.Chrome(service=s)
browser.get("https://github.com/")
time.sleep(2)
ara = browser.find_element(By.XPATH, value="/html/body/div[1]/div[1]/header/div/div[2]/div/div/qbsearch-input/div[1]/button/span").click()
time.sleep(2)
bul = browser.find_element(By.XPATH, value="//*[@id='query-builder-test']")
bul.send_keys(kişi)
bul.send_keys(Keys.ENTER)
time.sleep(5)
liste = browser.find_element(By.CSS_SELECTOR, "div[class='Box-sc-g0xbh4-0 kXssRI']")
ilk_sonuc = liste.find_element(By.TAG_NAME, "a").find_element(By.TAG_NAME, "span").text
if kişi in ilk_sonuc:
    liste.find_element(By.TAG_NAME, "a").click()
    
    time.sleep(3)
    
browser.close()