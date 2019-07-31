from selenium import webdriver
from selenium.webdriver.common.by import By
from SeleniumPractice.Handy_wrappers import HandyWrappers
import time


class ElementPresentCheck():

    def test(self):
        path = 'F:\\selenium-java-3.141.59\\geckodriver.exe'
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox(executable_path=path)
        driver.maximize_window()
        driver.implicitly_wait(10)
        hw = HandyWrappers(driver)
        driver.get(baseUrl)

        elementResult1 = hw.isElementPresent("name", By.ID)
        print(str(elementResult1))

        elementResult2 = hw.elementPresenceCheck("//input[@id='name1']", By.XPATH)
        print(str(elementResult2))


ff = ElementPresentCheck()
ff.test()