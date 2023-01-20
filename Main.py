from pystyle import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from time import sleep
import os
import json
import pyautogui as pag




config = open('config.json')
data = json.load(config)




os.system('cls & title Spotify ~ unofficialdxnny')



## headless = False
options = Options()
options.page_load_strategy = 'eager'
options.headless = False
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument("--log-level=OFF")
options.add_experimental_option("detach", True)
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--disable-notifications")

driver = webdriver.Chrome(options=options) ## Initialise the driver
driver.get("https://accounts.spotify.com/en/login?continue=https%3A%2F%2Faccounts.spotify.com%2Fen%2Fstatus") ## login to Spotify
## driver.maximize_window()
wait = WebDriverWait(driver, 100)



print('Loggingin to Spotify...')


with open('accounts.txt', 'r') as email:
    lines = email.readlines()
    for line in lines:

        driver.find_element(
            By.XPATH,
             '//*[@id="login-username"]'
         
             ).send_keys(
                line
             ) ## Email

        sleep(2)

        driver.find_element(
            By.XPATH,
             '//*[@id="login-password"]'
         
             ).send_keys(
                'BitzLol123'
             ) ## password

        sleep(2)

        driver.find_element(By.XPATH, '//*[@id="login-button"]').click() ## login button



        if 'status' in driver.current_url:
            print('opening webplayer')
            sleep(2)
            driver.get(data["playlist_url"])
            sleep(5)
            ## driver.find_element(By.XPATH, '//div[contains(@class,"ui-dialog") and @aria-describedby="dialogContent2"]//button[@title="Close"]').click() ## login button
            pag.keyDown('enter')
            pag.keyUp('enter')
            sleep(1)

            pag.keyDown('enter')
            pag.keyUp('enter')

            sleep(1)