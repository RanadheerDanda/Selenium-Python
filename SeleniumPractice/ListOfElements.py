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
            list_of_courses=driver.find_elements(By.XPATH,'//table[@id="product"]/tbody/tr/td[2]')
            #method1
            print('Printing list of courses using method 1\n')
            for x in list_of_courses:
                print(x.text)
            #method2
            print('\nPrinting list of courses using method 2\n')
            for i in range(len(list_of_courses)):
                print(list_of_courses[i].text)
            print('\nPrinting radio buttons using by Class and findelements method\n')
            list_of_radio_buttons=driver.find_elements(By.CLASS_NAME,'radioButton')
            for i in list_of_radio_buttons:
                print(i.get_attribute('value'))




test=FindByIDAndName()
test.find_by_id_and_name()