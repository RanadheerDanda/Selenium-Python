from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class GetAttribute():

    def test(self):
        path = 'F:\\selenium-java-3.141.59\\geckodriver.exe'
        baseUrl = 'https://learn.letskodeit.com/p/practice'
        driver = webdriver.Firefox(executable_path=path)
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(baseUrl)

        element = driver.find_element_by_id("name")
        result = element.get_attribute("type")

        print("Value of attribute is: " + result)
        time.sleep(1)
        driver.quit()




ff = GetAttribute()
ff.test()