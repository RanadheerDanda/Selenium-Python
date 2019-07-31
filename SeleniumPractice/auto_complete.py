from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class AutoComplete():

    def test(self):
        path = 'F:\\selenium-java-3.141.59\\geckodriver.exe'
        baseUrl = 'https://www.southwest.com/'
        driver = webdriver.Firefox(executable_path=path)
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        # Send Partial Data
        cityField = driver.find_element_by_id("LandingPageAirSearchForm_originationAirportCode")
        cityField.send_keys("New York")
        time.sleep(3)
        # Find the item and click
        itemToSelect = driver.find_element_by_xpath("//*[@id='TabbedArea_4-panel-0']/div/div/form/div[2]/div[1]/div[1]/label/div[3]")
        itemToSelect.click()

        # time.sleep(3)
        # driver.quit()

ff = AutoComplete()
ff.test()