#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import platform

# Variables
email = "anonymousbasketballplayer@gmail.com"
password = "dragon123456789"
friendName = "Anirudh Alahari"
sendDelay = 1;

# Checks if on Mac or Windows
if platform.system() == "Windows":
    driver = webdriver.Chrome('D:\Studies\Python\Facebook-Messenger-and-Whatsapp-message-spammer\chromedriver.exe')
else:
    driver = webdriver.Chrome()

# Opens Facebook Messenger
driver.get('https://www.messenger.com/')
time.sleep(4)

# Login
driver.find_element_by_xpath('//*[@id="email"]').send_keys(email)
driver.find_element_by_xpath('//*[@id="pass"]').send_keys(password)
driver.find_element_by_xpath('//*[@id="loginbutton"]').click()
# Waits 4 seconds to finish loading page
time.sleep(4)

# Gets user from conversation list
getUser = driver.find_element_by_xpath("//*[contains(text(), '" + friendName + "')]").click()

# Reads Shrek script file and saves to movie_script list
movie_script = []
with open('D:\Studies\Python\Facebook-Messenger-and-Whatsapp-message-spammer\script.txt', "r", encoding="utf-8") as f:
    for line in f.readlines():
            print(line)
            actions = ActionChains(driver)
            actions.send_keys(line, Keys.ENTER)
            actions.perform()
            time.sleep(sendDelay)
#for word in line.split():
#encoding="utf-8"
