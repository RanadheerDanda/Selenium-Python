from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import time

class ExplicitWaitWithCalender:
        def explicit_wait_demo(self):
            path='F:\\selenium-java-3.141.59\\geckodriver.exe'
            baseUrl='https://www.expedia.co.in/'
            driver = webdriver.Firefox(executable_path=path)
            driver.get(baseUrl)
            driver.maximize_window()
            driver.implicitly_wait(2)
            flights_tab = driver.find_element(By.XPATH,'//button[@id="tab-flight-tab-hp"]')
            flights_tab.click()
            one_way = driver.find_element(By.XPATH,'//label[@id="flight-type-one-way-label-hp-flight"]')
            one_way.click()
            time.sleep(5)

            from_box = driver.find_element(By.XPATH,"//input[@id='flight-origin-hp-flight']")
            from_box.send_keys("bangalore",Keys.ENTER)
            to_box = driver.find_element(By.XPATH,"//input[@id='flight-destination-hp-flight']")
            to_box.send_keys('Hyderabad',Keys.ENTER)
            from_date = driver.find_element(By.XPATH,'//input[@id="flight-departing-single-hp-flight"]')
            from_date.click()
            time.sleep(2)
            date_to_select = driver.find_element(By.XPATH,'(//table[@class="datepicker-cal-weeks"])[1]//button[contains(text(),"31")]')
            date_to_select.click()
            time.sleep(5)
            serach_button = driver.find_element(By.XPATH,'//*[@id="gcw-flights-form-hp-flight"]/div[8]/label/button')
            serach_button.click()

            wait =WebDriverWait(driver,20,poll_frequency=5,ignored_exceptions=[NoSuchElementException,ElementNotVisibleException,ElementNotSelectableException ])
            element = wait.until(EC.element_to_be_clickable((By.XPATH,'//input[@id="airlineRowContainer_UK"]')))
            element.click()





test=ExplicitWaitWithCalender()
test.explicit_wait_demo()