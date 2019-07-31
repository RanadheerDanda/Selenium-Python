from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import time

class Screenshot:
        def test_screenshot(self):
            path='F:\\selenium-java-3.141.59\\geckodriver.exe'
            baseUrl='https://learn.letskodeit.com/'
            driver = webdriver.Firefox(executable_path=path)
            driver.get(baseUrl)
            driver.maximize_window()
            driver.implicitly_wait(2)
            driver.find_element(By.LINK_TEXT,'Login').click()
            time.sleep(5)
            driver.find_element(By.XPATH,'//input[@type="email"]').send_keys('drr.nani@gmail.com')
            driver.find_element(By.XPATH,'//input[@type="password"]').send_keys('abcabc2')
            driver.find_element(By.XPATH,'//input[@type="submit"]').click()
            screenshot_path = 'F:\\PythonPractice\\SeleniumPractice\\test1.png'
            try:
                driver.save_screenshot(screenshot_path)
                print("Screenshot is created at", screenshot_path)
            except NotADirectoryError:
                print('directory issues')
            else:
                print('No errors')
            finally:
                print('Finally block is executed')






test=Screenshot()
test.test_screenshot()