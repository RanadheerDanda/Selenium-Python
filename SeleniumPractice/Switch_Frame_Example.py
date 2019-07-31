from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

from selenium import webdriver


class FrameWorksExample:
        def test_frameworks(self):
            path='F:\\selenium-java-3.141.59\\geckodriver.exe'
            baseUrl='https://learn.letskodeit.com/p/practice'
            driver = webdriver.Firefox(executable_path=path)
            driver.get(baseUrl)
            #driver.set_page_load_timeout(10)
            driver.implicitly_wait(10)
            driver.maximize_window()
            driver.execute_script("window.scrollBy(0,1400);")
            #switch to the frame by id
            #driver.switch_to.frame("courses-iframe")
            #switch to the frame by name
            driver.switch_to.frame("iframe-name")
            #switch to the frame by locator


            search_box = driver.find_element(By.XPATH, '//input[@id="search-courses"]')
            search_box.send_keys('python')
            time.sleep(2)
            _course = "//div[contains(@class,'course-listing-title') and contains(text(),'Learn Python 3 from scratch')]"
            courseElement = driver.find_element(By.XPATH, _course)
            courseElement.click()
            time.sleep(5)
            driver.find_element(By.XPATH,'//a[@id="watchpromo"]').click()
            time.sleep(5)


            driver.switch_to.default_content()
            driver.find_element(By.LINK_TEXT,'Login').click()

            time.sleep(10)



test=FrameWorksExample()
test.test_frameworks()