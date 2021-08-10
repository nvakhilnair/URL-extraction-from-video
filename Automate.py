import os
from selenium import webdriver

def web_Automate(urls):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-gpu")
    chrome_Driver_Dir = os.getcwd() + '/Linux_chromedriver'
    browser = webdriver.Chrome(chrome_Driver_Dir,options = chrome_options)
    browser.get(urls[0])

    for i in range(1,len(urls)):
        browser.execute_script("window.open();")
        browser.switch_to.window(browser.window_handles[i])
        browser.get(urls[i])
