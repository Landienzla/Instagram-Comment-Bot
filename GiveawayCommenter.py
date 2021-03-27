from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import pyautogui
import time
import itertools

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://www.instagram.com")
time.sleep(15)
browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').click()
time.sleep(15)
pyautogui.write("your-username")
browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').click()
time.sleep(15)
pyautogui.write("your-password")
browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]').click()
time.sleep(15)
browser.get("giveaway link")
time.sleep(15)

userlist= [""]
combineduserlist = list(itertools.combinations(userlist,2))
a = 34
for i in range(325):
    browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[3]').click()
    commentarea = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea')
    commentarea.send_keys(combineduserlist[a])
    time.sleep(10)
    browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[3]/div/form/button').click()
    print(combineduserlist[a], a , ".Yorum")
    a += 1
    time.sleep(60)
browser.stop_client()
browser.close()

















