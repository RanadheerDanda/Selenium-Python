from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class JavaScriptExecution():

    def test(self):
        path = 'F:\\selenium-java-3.141.59\\geckodriver.exe'
        #baseUrl = 'https://learn.letskodeit.com/'
        driver = webdriver.Firefox(executable_path=path)
        #driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(2)
        # driver.get("https://letskodeit.teachable.com/pages/practice")
        driver.execute_script("window.location = 'https://letskodeit.teachable.com/pages/practice';")
        driver.implicitly_wait(3)
        time.sleep(6)

        # element = driver.find_element(By.ID, "name")
        element = driver.execute_script("return document.getElementById('name');")
        element.send_keys("Test")

ff = JavaScriptExecution()
ff.test()