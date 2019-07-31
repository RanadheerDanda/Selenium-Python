from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

class HiddenElements:
    path = 'F:\\selenium-java-3.141.59\\geckodriver.exe'
    baseUrl = 'http://www.qaclickacademy.com/practice.php'
    driver = webdriver.Firefox(executable_path=path)

    def test(self):
        my_driver = self.driver
        my_driver.get(self.baseUrl)
        my_driver.maximize_window()
        my_driver.implicitly_wait(5)
        text_box = my_driver.find_element(By.XPATH,'//input[@id="displayed-text"]')
        text_box.send_keys('Ranadheer')
        print('text box is enabled ?',str(text_box.is_enabled()))
        print('text box is displayed ', str(text_box.is_displayed()))
        time.sleep(3)
        my_driver.find_element(By.XPATH,'//input[@id="hide-textbox"]').click()
        print('after clicking on hide button')
        print('text box is enabled ?', str(text_box.is_enabled()))
        print('text box is displayed ', str(text_box.is_displayed()))
        time.sleep(3)
        my_driver.find_element(By.XPATH, '//input[@id="show-textbox"]').click()
        print('after clicking on show button')
        print('text box is enabled ?', str(text_box.is_enabled()))
        print('text box is displayed ', str(text_box.is_displayed()))
        time.sleep(3)
        self.driver.quit()


    def expedia(self):
        driver2=self.driver
        baseurl ='https://www.expedia.co.in/India.d80.Holidays-City-Breaks'
        driver2.get(baseurl)
        driver2.find_element(By.XPATH,'//button[@id="tab-flight"]').click()
        time.sleep(2)
        children = driver2.find_element(By.XPATH,'//select[@id="F-NumChild"]')
        sel_children = Select(children)
        sel_children.select_by_value('1')
        time.sleep(2)
        child1 = driver2.find_element(By.XPATH,'//select[@id="F-Age1"]')
        print(str(child1.is_displayed()))
        sel_child1 = Select(child1)
        sel_child1.select_by_value('2')
        driver2.quit()












test=HiddenElements()
test.expedia()