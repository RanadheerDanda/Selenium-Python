from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

from selenium import webdriver


class WindowHandler:
        def test_window(self):
            path='F:\\selenium-java-3.141.59\\geckodriver.exe'
            baseUrl='https://learn.letskodeit.com/p/practice'
            driver = webdriver.Firefox(executable_path=path)
            driver.get(baseUrl)
            #driver.set_page_load_timeout(10)
            driver.implicitly_wait(10)
            driver.maximize_window()
            table = driver.find_elements_by_xpath('//table/tbody/tr/td[1]/ul/li/a')
            print("before switching the parent window title is ", driver.title)
            parent_handle = driver.current_window_handle
            print("Parent window id is ", parent_handle)
            driver.find_element(By.XPATH,'//button[@id="openwindow"]').click()
            time.sleep(2)

            handles = driver.window_handles
            for handle in handles:
                print('Handle id :' , handle)
                if handle not in parent_handle:
                    driver.switch_to.window(handle)
                    search_box = driver.find_element(By.XPATH,'//input[@id="search-courses"]')
                    search_box.send_keys('python')
                    time.sleep(2)
                    _course = "//div[contains(@class,'course-listing-title') and contains(text(),'{0}')]"
                    _courseLocator = _course.format("Learn Python 3 from scratch")

                    courseElement = driver.find_element(By.XPATH, _courseLocator)
                    courseElement.click()

                    driver.find_element(By.XPATH,'//a[@id="watchpromo"]').click()
                    time.sleep(5)
                    driver.close()



            print("switching to parent window")
            driver.switch_to.window(parent_handle)
            driver.find_element(By.LINK_TEXT,'Login').click()
            print( " title is " , driver.title)




            time.sleep(10)



test=WindowHandler()
test.test_window()