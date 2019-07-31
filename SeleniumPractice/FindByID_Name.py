from selenium import webdriver
import time

class FindByIDAndName:
        def find_by_id_and_name(self):
            path='F:\\selenium-java-3.141.59\\geckodriver.exe'
            baseUrl='http://www.qaclickacademy.com/practice.php'
            driver = webdriver.Firefox(executable_path=path)
            driver.get(baseUrl)
            text_box = driver.find_element_by_name('enter-name')
            text_box.send_keys("RanadheerReddyDanda")
            button = driver.find_element_by_id('alertbtn')
            button.click()
            alert_text=driver.switch_to.alert.text
            time.sleep(10)
            driver.switch_to.alert.accept()
            print(alert_text)


test=FindByIDAndName()
test.find_by_id_and_name()