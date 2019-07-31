from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

class DropDowns:
    path = 'F:\\selenium-java-3.141.59\\geckodriver.exe'
    baseUrl = 'http://demo.guru99.com/test/newtours/register.php'
    driver = webdriver.Firefox(executable_path=path)

    def Single_Select_Dropdowns(self):
        my_driver = self.driver
        my_driver.get(self.baseUrl)
        my_driver.maximize_window()
        my_driver.implicitly_wait(5)
        country_dropdown = my_driver.find_element(By.XPATH, '//select[@name="country"]')
        sel = Select(country_dropdown)
        sel.select_by_index(6)
        time.sleep(2)
        sel.select_by_value('INDIA')
        time.sleep(2)
        sel.select_by_visible_text('UNITED STATES')
        self.driver.quit()


    def Multi_Select_drpdwn(self):
        driver2=self.driver
        baseurl ='http://output.jsbin.com/osebed/2'
        driver2.get(baseurl)
        multi_drpdwn = driver2.find_element(By.ID,'fruits')
        sel = Select(multi_drpdwn)
        sel.select_by_visible_text('Banana')
        time.sleep(2)
        sel.select_by_value('grape')
        time.sleep(2)
        sel.select_by_index(1)
        time.sleep(2)
        sel.deselect_all()
        time.sleep(5)
        print(sel.all_selected_options)
        options1=sel.options

        for i in range(len(options1)):
            print(options1[i])












test=DropDowns()
test.Multi_Select_drpdwn()