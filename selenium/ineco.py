from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
import time


# options = Options()
# options.add_argument('--headless=new')
try:
    driver = webdriver.Chrome()
    driver.get(url='https://arlis.am/hy/')
    driver.maximize_window()
    time.sleep(2)
    # time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, 'body > main > div.home-main > div.home-links > div > div:nth-child(2) > div > div:nth-child(2) > div > div > a').click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, 'body > main > div > div > div > div.column.small-14.large-12 > div > div > div:nth-child(12) > a').click()
    time.sleep(10)
    lows = driver.find_element(By.CLASS_NAME, 'act-content')
    print(lows)
    # driver.find_element(By.CSS_SELECTOR, '#root > div > div > div > div.header__wrapper__layout > div > nav > ul > li:nth-child(2) > div > div > ul:nth-child(1) > li:nth-child(2) > a').click()
    # time.sleep(5)
except Exception as error:
    print(error)
finally:
    driver.close()
    driver.quit()