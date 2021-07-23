from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome(executable_path='../driver/chromedriver', options=chrome_options)

LOGIN_URL = 'https://dodofile.com/'
LOGIN_EMAIL = 'email'
LOGIN_PW = 'pw'


driver.get(LOGIN_URL)
driver.find_element_by_id('mb_id').send_keys(LOGIN_EMAIL)
driver.find_element_by_id('mb_pw').send_keys(LOGIN_PW + Keys.ENTER)

sleep(4)

popUp = driver.find_element_by_css_selector('.olw_back')
driver.execute_script("arguments[0].click();", popUp)
