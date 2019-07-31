from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class AlertDemo:
        def Test_Alert(self):
            path='F:\\selenium-java-3.141.59\\geckodriver.exe'
            baseUrl='http://demo.guru99.com/test/delete_customer.php'
            driver = webdriver.Firefox(executable_path=path)
            driver.get(baseUrl)
            driver.implicitly_wait(10)
            driver.maximize_window()
            driver.find_element(By.NAME,'cusid').send_keys('53920')
            driver.find_element(By.NAME,"submit").submit()
            time.sleep(5)
            alert_msg= driver.switch_to.alert.text
            print("alert message is ", alert_msg)
            driver.switch_to.alert.accept()
            time.sleep(5)




test=AlertDemo()
test.Test_Alert()