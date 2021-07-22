from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('headless')

driver = webdriver.Chrome('../driver/chromedriver', options=options)
driver.get('https://www.google.com')
driver.save_screenshot('./pictures/google.png')

driver.close()