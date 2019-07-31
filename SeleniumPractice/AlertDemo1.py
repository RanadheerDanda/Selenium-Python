from selenium import webdriver
import time

class AlertDemo1:
        def test_alert(self):
            path='F:\\selenium-java-3.141.59\\geckodriver.exe'
            baseUrl='http://www.qaclickacademy.com/practice.php'
            driver = webdriver.Firefox(executable_path=path)
            driver.get(baseUrl)
            driver.maximize_window()
            driver.implicitly_wait(10)
            #Test alert by clicking on alert button
            text_box = driver.find_element_by_name('enter-name')
            text_box.send_keys("RanadheerReddyDanda")
            alert_button = driver.find_element_by_id('alertbtn')
            alert_button.click()
            Alert1=driver.switch_to.alert
            alert_text =Alert1.text
            time.sleep(5)
            Alert1.accept()
            print(alert_text)
            # test alert by clicking on confirm button
            text_box = driver.find_element_by_name('enter-name')
            text_box.send_keys("RanadheerReddy")
            confirm_button = driver.find_element_by_id('confirmbtn')
            confirm_button.click()
            Alert2 = driver.switch_to.alert
            msg = Alert2.text
            time.sleep(5)
            print(msg)
            Alert2.dismiss()


test=AlertDemo1()
test.test_alert()