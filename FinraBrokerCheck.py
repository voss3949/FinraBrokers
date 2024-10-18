import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("https://brokercheck.finra.org/individual/summary/" + "2928202")

sourcetext = browser.page_source
PrevRegister = "Previously Registered" in sourcetext
print("Previously a Broker") if PrevRegister == True else "Currently a Broker"


BrokerAddress = browser.find_element(By.TAG_NAME, 'investor-tools-address').text.replace("\n", "")
print(BrokerAddress)
BrokerAddress = browser.find_element(By.TAG_NAME, 'investor-tools-address').text.replace("\n", "")
print(BrokerAddress)

