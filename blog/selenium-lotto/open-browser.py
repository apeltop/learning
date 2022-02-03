from selenium import webdriver
from selenium.webdriver.chrome.service import Service


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


close_windows_if_not_main_url('common.do?method=main')
