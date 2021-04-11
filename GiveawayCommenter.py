from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import pyautogui
import time
import itertools

browser = webdriver.Chrome(ChromeDriverManager().install()) # install last version of chrome
browser.get("https://www.instagram.com") #get instagram page at browser
time.sleep(15) 
username_area = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
username_area.click()
time.sleep(15)
username_area.send_keys("username")
password_area = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
password_area.click()
time.sleep(15)
password_area.send_keys("password")
browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]').click()
time.sleep(15)
browser.get("the giveaway's link")
time.sleep(15)

userlist= [""]
combineduserlist = list(itertools.combinations(userlist,2))
for i in range(len(combineduserlist)):
    try:
        browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[3]').click()
        commentarea = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea')
        commentarea.send_keys(combineduserlist[i])
        time.sleep(10)
        browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[3]/div/form/button[2]').click()
        time.sleep(60)
    except:
        print("ERROR")
        print("I was commenting" + combineduserlist[i])
browser.stop_client()
browser.close()

















