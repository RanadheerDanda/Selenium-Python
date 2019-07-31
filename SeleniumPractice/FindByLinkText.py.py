from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class FindByIDAndName:
        def find_by_id_and_name(self):
            path='F:\\selenium-java-3.141.59\\geckodriver.exe'
            baseUrl='http://www.qaclickacademy.com/practice.php'
            driver = webdriver.Firefox(executable_path=path)
            driver.get(baseUrl)
            header=driver.find_element_by_tag_name('h1')
            print(header.text)
            rest_api=driver.find_element_by_link_text('REST API')
            rest_api.send_keys(Keys.CONTROL,Keys.ENTER)
            SoapUI=driver.find_element_by_partial_link_text('Soap')
            SoapUI.click()



test=FindByIDAndName()
test.find_by_id_and_name()