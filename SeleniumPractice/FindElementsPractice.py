from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

from selenium import webdriver


class FindByIDAndName:
        def find_by_id_and_name(self):
            path='F:\\selenium-java-3.141.59\\geckodriver.exe'
            baseUrl='http://www.qaclickacademy.com/practice.php'
            driver = webdriver.Firefox(executable_path=path)
            driver.get(baseUrl)
            #driver.set_page_load_timeout(10)
            driver.implicitly_wait(10)
            driver.maximize_window()
            table = driver.find_elements_by_xpath('//table/tbody/tr/td[1]/ul/li/a')
            print("before switching the parent window title is ", driver.title)
            parent_handle = driver.current_window_handle
            print("Parent window id is ", parent_handle)

            for link in table:
                print(link.get_attribute('href'))
                link.send_keys(Keys.CONTROL+Keys.ENTER)
            time.sleep(5)
            handles = driver.window_handles
            size = len(handles)

            """ using over a loop
            for x in range(size):
                print(driver.title)
                driver.switch_to.window(handles[x])
                """
            for x in handles:
                driver.switch_to.window(x)
                print("window id :", x ," title is :",str(driver.title))
                title = str(driver.title)
                if 'REST' in title:
                    driver.find_element(By.LINK_TEXT,"HTTP Status Codes").click()
                    time.sleep(5)
                elif "SoapUI" in title:
                    driver.find_element(By.XPATH,'// ul[ @ id = "menuElem"] // child::li // a[contains( @ role, "button")]').click()
                    time.sleep(5)
                    driver.find_element(By.PARTIAL_LINK_TEXT,'Load Testing').click()
                elif 'Appium' in title:
                    driver.find_element(By.LINK_TEXT,'Introduction').click()
                    time.sleep(5)
                elif 'Apache' in title:
                    driver.find_element(By.LINK_TEXT,'License').click()
                    time.sleep(5)
                else:
                    pass


                time.sleep(5)
            print("switching to parent window")
            driver.switch_to.window(parent_handle)
            print( " title is " , driver.title)




            time.sleep(10)



test=FindByIDAndName()
test.find_by_id_and_name()