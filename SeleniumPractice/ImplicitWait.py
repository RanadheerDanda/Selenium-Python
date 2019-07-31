from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ImplicitWait:
        def implicit_wait_demo(self):
            path='F:\\selenium-java-3.141.59\\geckodriver.exe'
            baseUrl='https://learn.letskodeit.com/'
            driver = webdriver.Firefox(executable_path=path)
            driver.get(baseUrl)
            driver.maximize_window()
            driver.implicitly_wait(10)
            driver.find_element(By.XPATH,'//a[contains(@href,"sign_in")]').click()
            email= driver.find_element(By.XPATH,'//input[@id="user_email"]')
            email.send_keys("drr.nani@gmail.com")
            time.sleep(5)
            email.clear()
            driver.quit()





test=ImplicitWait()
test.implicit_wait_demo()