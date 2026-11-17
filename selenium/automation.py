from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    driver = webdriver.Chrome()
    driver.get(url='https://smartcode.am/hy/#close')
    driver.maximize_window()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, 'body > main > header > div > div > div > a.but-main').click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, 'body > div.overlay > div > div.overlay-body > form > p:nth-child(2) > select > option:nth-child(4)').click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, 'body > div.overlay > div > div.overlay-body > form > p:nth-child(3) > input[type=text]').send_keys('Shavarsh Karapetyan')
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, 'body > div.overlay > div > div.overlay-body > form > p:nth-child(4) > input[type=mail]').send_keys('ShavarshKarapetyan19@gmail.com')
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, 'body > div.overlay > div > div.overlay-body > form > p:nth-child(5) > input[type=tel]').send_keys('043088878')
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, 'body > div.overlay > div > div.overlay-body > form > p:nth-child(6) > select > option:nth-child(2)').click()
    time.sleep(4)
except Exception as error:
    print(error)
finally:
    driver.close()
    driver.quit()
    
    