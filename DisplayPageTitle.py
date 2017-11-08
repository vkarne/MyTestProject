#  Contents of DisplayPageTitle.py


from selenium import webdriver
import time

def launchFirefox():
    browser = webdriver.Chrome()
    url = "https://google.com"

    browser.get(url)
    print(browser.title)

    time.sleep(2)
    browser.close()

def launchChrome():
    browser = webdriver.Chrome()
    url = "http://seleniumhq.com"

    browser.get(url)
    print(browser.title)

    time.sleep(2)
    browser.close()

launchFirefox()
launchChrome()

