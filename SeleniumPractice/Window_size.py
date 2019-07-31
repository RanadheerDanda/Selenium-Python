from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class WindowSize():

    def test(self):
        path = 'F:\\selenium-java-3.141.59\\geckodriver.exe'
        baseUrl = 'https://learn.letskodeit.com/'
        driver = webdriver.Firefox(executable_path=path)
        driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(2)


        height = driver.execute_script("return window.innerHeight;")
        width = driver.execute_script("return window.innerWidth;")
        print("Height: " + str(height))
        print("Width: " + str(width))
        driver.quit()


ff = WindowSize()
ff.test()