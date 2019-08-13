# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

import time
import random


chrome_options = Options() 
chrome_options.add_argument('–headless') 
chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"




url = 'https://www.xuexi.cn/'
shipin_url ='https://www.xuexi.cn/a191dbc3067d516c3e2e17e2e08953d6/b87d700beee2c44826a9202c75d18c85.html'
xinshijie_url2 = 'https://www.xuexi.cn/0b99b2eb0a13e4501cbaf82a5c37a853/b87d700beee2c44826a9202c75d18c85.html' 

browser = webdriver.Chrome(chromedriver,chrome_options=chrome_options)
browser.implicitly_wait(10)
count = 0
try:
    browser.get(url)
    buttons = browser.find_elements_by_class_name("_3wnLIRcEni99IWb4rSpguK")
    for button in buttons:
        button.click()
        time.sleep(2)
        browser.switch_to_window(browser.window_handles[1])
        time.sleep(2)
        browser.execute_script('window.scrollTo(0,400)')
        time.sleep(random.randint(1,10))
        browser.execute_script('window.scrollTo(0,500)')
        time.sleep(random.randint(1,10))
        browser.execute_script('window.scrollTo(0,550)')
        time.sleep(random.randint(1,10))
        browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(1)
        browser.execute_script('window.close()')
        browser.switch_to_window(browser.window_handles[0])
        count +=1
        if count ==6:
            break
    browser.get(shipin_url)
    bus = browser.find_elements_by_class_name("_3wnLIRcEni99IWb4rSpguK")
    for button in bus:
        button.click()
        time.sleep(1)
        browser.switch_to_window(browser.window_handles[1])
        time.sleep(2)
        browser.execute_script('window.scrollTo(0,400)')
        time.sleep(random.randint(1,10))
        browser.execute_script('window.scrollTo(0,500)')
        time.sleep(random.randint(10,30))
        browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(1)
        browser.execute_script('window.close()')
        browser.switch_to_window(browser.window_handles[0])
        count +=1
        if count ==6:
            break
    
    
finally:
    browser.close()
