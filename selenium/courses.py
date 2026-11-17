from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


options = Options()
options.add_argument('--headless=new')
try:
    driver = webdriver.Chrome(options=options())
    driver.get(url='https://smartcode.am/hy/#close')
    driver.maximize_window()
    time.sleep(3)
    with open('courses.txt', 'w', encoding='UTF-8') as f:
        for page in range(2, 7):
            time.sleep(2)
            courses = driver.find_elements(By.CLASS_NAME, 'course-item')
            for course in courses:
                if course.text:
                    f.write('-' * 50 + '\n')
                    f.write(course.text + '\n')
            driver.find_element(By.CSS_SELECTOR, f'body > main > section.courses.bg-silver > div > div.section-box > div > ul > li:nth-child({page})').click()
except Exception as error:
    print(error)
finally:
    driver.close()
    driver.quit()