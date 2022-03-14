from datetime import datetime
import random
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from dotenv import load_dotenv
import os

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()

LOTTO_MIN_NUM = 1
LOTTO_MAX_NUM = 45


def create_driver():
    return webdriver.Chrome(service=Service('./driver/chromedriver_mac64_m1_97'))


driver = create_driver()
driver.get('https://dhlottery.co.kr/common.do?method=main')


def get_main_handle(main_url):
    for window_handle in driver.window_handles:
        driver.switch_to.window(window_handle)

        print(f'현재 핸들러 name : {driver.current_window_handle}')
        print(f'현재 url :  {driver.current_url}')
        print('')

        if main_url in driver.current_url:
            return window_handle
    raise '메인 핸들러 찾지 못함'


def close_windows_if_not_main_url(main_url):
    main_handle = get_main_handle(main_url)

    for window_handle in driver.window_handles:
        if main_handle != window_handle:
            driver.switch_to.window(window_handle)
            driver.close()

    driver.switch_to.window(main_handle)


def send_keys(element, text):
    element.send_keys(text)


def click(element):
    element.click()


def execute_script(script):
    driver.execute_script(script)


def switch_to_last_opened_window():
    driver.switch_to.window(driver.window_handles[-1])


def switch_to_iframe(iframe):
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "iframe"))
    )

    driver.switch_to.frame(iframe)


def pick_numbers():
    picks = set([])
    while 6 != len(picks):
        n = random.randint(LOTTO_MIN_NUM, LOTTO_MAX_NUM)
        picks.add(n)

    return picks


def save_screenshot():
    driver.save_screenshot(f'{datetime.now().strftime("%Y%m%d_%H%M%S")}.png')


close_windows_if_not_main_url('common.do?method=main')

click(driver.find_element(By.XPATH, '/html/body/div[1]/header/div[2]/div[2]/form/div/ul/li[1]/a'))

send_keys(driver.find_element(By.ID, 'userId'), os.environ.get('ID'))
send_keys(driver.find_element(By.NAME, 'password'), os.environ.get('PW'))
send_keys(driver.find_element(By.NAME, 'password'), Keys.ENTER)

sleep(1)

close_windows_if_not_main_url('common.do?method=main')

execute_script('goLottoBuy(2);')

sleep(1)

switch_to_last_opened_window()

switch_to_iframe(driver.find_elements(By.TAG_NAME, 'iframe')[0])

for num in pick_numbers():
    execute_script(f'$("#check645num{num}").prop("checked", true);')

click(driver.find_element(By.ID, 'btnSelectNum'))

click(driver.find_element(By.ID, 'btnBuy'))
execute_script('closepopupLayerConfirm(true);')

sleep(2)
save_screenshot()

driver.quit()
