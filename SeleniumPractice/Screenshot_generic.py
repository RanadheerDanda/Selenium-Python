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
            self.takeScreenshot(driver)

        def takeScreenshot(self, driver):
            """
            Takes screenshot of the current open web page
            :param driver
            :return:
            """
            fileName = str(round(time.time() * 1000)) + ".png"
            screenshotDirectory = "F:\\PythonPractice\\SeleniumPractice\\"
            destinationFile = screenshotDirectory + fileName

            try:
                driver.save_screenshot(destinationFile)
                print("Screenshot saved to directory --> :: " + destinationFile)
            except NotADirectoryError:
                print("Not a directory issue")






test=Screenshot()
test.test_screenshot()