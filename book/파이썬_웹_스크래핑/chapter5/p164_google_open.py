from selenium import webdriver

driver = webdriver.Chrome(executable_path='../driver/chromedriver')
driver.get('https://www.google.com')