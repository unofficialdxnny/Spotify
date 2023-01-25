from pystyle import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from time import sleep
import keyboard as kb
import os
import json



f = open('config.json')

data = json.load(f)

banner = '''





'''


os.system('cls & title SpotGen ~ unofficialdxnny')
Write.Print(f"{banner}", Col.DynamicMIX((Col.white, Col.yellow)) 
, interval=0)


## headless = False
options = Options()
options.page_load_strategy = 'eager'
## options.headless = headless
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument("--log-level=OFF")
options.add_experimental_option("detach", True)
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(options=options) ## Initialise the driver
driver.get("https://accounts.spotify.com/en/login?continue=https%3A%2F%2Fopen.spotify.com%2F")
## driver.maximize_window()
wait = WebDriverWait(driver, 100)


while True:

    

    sleep(5)
    with open('accounts.txt', 'r') as acc:
        sleep(5)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/input').clear() ## clear email
        lines = acc.readlines()
        for line in lines:
            sleep(5)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/input').send_keys(line) ## email
            sleep(2)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[1]/div[2]/input').clear() ## clear pwd
            sleep(2)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[1]/div[2]/input').send_keys('unofficialdxnnyiscool') ## pwd
            sleep(5)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[1]/div[3]/div[2]/button').click() ## login
            sleep(5)

            driver.get(f'https://open.spotify.com/playlist/{data["playlist_url_code"]}')
            sleep(5)    
            driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div/section/div[2]/div[2]/div[4]/div/div/div/div/button[1]').click() ## like playlist   
            driver.get(f'https://open.spotify.com/user/{data["username_to_follow"]}')
            sleep(5)
            driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/section/div/div[3]/div[4]/div/div/div/div/button[1]').click() ## follow user
    
    
            driver.find_element(By.CLASS_NAME, 'odcjv30UQnjaTv4sylc0').click() ## dropdown
            sleep(5)
    
            driver.find_element(By.XPATH, '/html/body/div[14]/div/div/ul/li[5]').click() ## logout
    
            sleep(5)
            driver.get("https://accounts.spotify.com/en/login?continue=https%3A%2F%2Fopen.spotify.com%2F")
            sleep(5)
    
## while True:
##     Login()
##     interact()