from selenium import webdriver
import time

class FindByXpath:
        def find_by_id_and_name(self):
            path='F:\\selenium-java-3.141.59\\geckodriver.exe'
            baseUrl='https://jqueryui.com/droppable/'
            driver = webdriver.Firefox(executable_path=path)
            driver.get(baseUrl)
            text_box = driver.find_element_by_xpath('//input[@id="name"]')
            text_box.send_keys("RanadheerReddyDanda")
            button = driver.find_element_by_id('alertbtn')
            button.click()

            alert_text=driver.switch_to.alert.text
            time.sleep(10)
            driver.switch_to.alert.accept()
            print(alert_text)
            time.sleep(5)
            show_hide=driver.find_element_by_xpath('//input[@id="displayed-text"]')
            show_hide.send_keys('Ranadheer')
            driver.find_element_by_xpath('//input[@id="hide-textbox"]').click()
            driver.find_element_by_xpath('//input[@id="show-textbox"]').click()
            time.sleep(10)
            show_hide.clear()



test=FindByXpath()
test.find_by_id_and_name()