from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class FindByIDAndName:
        def find_by_id_and_name(self):
            path='F:\\selenium-java-3.141.59\\geckodriver.exe'
            baseUrl='http://www.qaclickacademy.com/practice.php'
            driver = webdriver.Firefox(executable_path=path)
            driver.get(baseUrl)
            text_box = driver.find_element(By.XPATH,'//input[@id="name"]')
            text_box.send_keys("RanadheerReddyDanda")
            button = driver.find_element(By.ID,'alertbtn')
            button.click()

            time.sleep(3)
            alert_text = driver.switch_to.alert.text
            driver.switch_to.alert.accept()
            print(alert_text)
            time.sleep(5)
            show_hide=driver.find_element(By.ID,"displayed-text")
            show_hide.send_keys('Ranadheer')
            driver.find_element(By.XPATH,'//input[@id="hide-textbox"]').click()
            driver.find_element(By.XPATH,'//input[@id="show-textbox"]').click()
            time.sleep(5)
            show_hide.clear()
            time.sleep(5)
            rest_api = driver.find_element(By.LINK_TEXT,'REST API')
            rest_api.send_keys(Keys.CONTROL, Keys.ENTER)
            SoapUI = driver.find_element(By.PARTIAL_LINK_TEXT,'Soap')
            SoapUI.click()



test=FindByIDAndName()
test.find_by_id_and_name()