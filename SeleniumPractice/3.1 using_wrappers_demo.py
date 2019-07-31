from selenium import webdriver
from SeleniumPractice.Handy_wrappers import HandyWrappers
import time


class UsingWrappers1():

    def test(self):
        path = 'F:\\selenium-java-3.141.59\\geckodriver.exe'
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox(executable_path=path)
        driver.maximize_window()
        driver.implicitly_wait(10)
        hw = HandyWrappers(driver)
        driver.get(baseUrl)

        textField1 = hw.getElement("name")
        textField1.send_keys("Test")
        time.sleep(2)
        textField2 = hw.getElement("//input[@id='name']", locatorType="xpath")
        textField2.clear()

ff = UsingWrappers1()
ff.test()