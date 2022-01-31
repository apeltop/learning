from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service('./driver/chromedriver_mac64_m1_97'))
driver.get('https://www.google.com')
