from selenium import webdriver
from selenium.webdriver.common.by import By

import time

class ClickAndSendKeys():

    def test(self):
        path = 'F:\\selenium-java-3.141.59\\geckodriver.exe'
        baseUrl = "https://letskodeit.teachable.com"
        driver = webdriver.Firefox(executable_path=path)
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)



        loginLink = driver.find_element(By.XPATH, "//div[@id='navbar']//a[@href='/sign_in']")
        loginLink.click()

        emailField = driver.find_element(By.ID, "user_email")
        emailField.send_keys("test")

        passwordField = driver.find_element(By.ID, "user_password")
        passwordField.send_keys("test")

        time.sleep(3)

        emailField.clear()
        passwordField.clear()

        time.sleep(3)

        emailField.send_keys("test@gmail.com")
        passwordField.send_keys('password')
        login_btn =driver.find_element(By.XPATH,'//input[@type="submit"]')
        login_btn_check=login_btn.is_enabled()
        if login_btn_check is True:
            print('login butoon check is',login_btn_check)
            login_btn.click()

        error_msg=driver.find_element(By.XPATH,'//div[contains(@class,"alert-danger")]')
        print(error_msg.text)




ff = ClickAndSendKeys()
ff.test()