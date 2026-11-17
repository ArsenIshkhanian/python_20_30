from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
import time


# options = Options()
# options.add_argument('--headless=new')
try:
    driver = webdriver.Chrome()
    driver.get(url='https://smartcode.am/hy/#close')
    driver.maximize_window()
    content = driver.find_elements(By.CLASS_NAME, 'staff-item')
    with open('Lecturers.txt', 'w', encoding='utf-8') as f:
        for member in content:
            # member = driver.find_element(By.CSS_SELECTOR, f'body > main > section.staff.bg-silver > div > div.section-box > div > div:nth-child({i})')
            f.write('-' * 50 + '\n')
            f.write(member.text + '\n')
except Exception as error:
    print(error)
finally:
    driver.close()
    driver.quit()