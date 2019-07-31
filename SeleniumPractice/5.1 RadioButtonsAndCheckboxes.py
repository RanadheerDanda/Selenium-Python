from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class RadioButtonsAndCheckboxes():

    def test(self):
        path = 'F:\\selenium-java-3.141.59\\geckodriver.exe'
        baseUrl = 'https://learn.letskodeit.com/p/practice'
        driver = webdriver.Firefox(executable_path=path)
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        bmwRadioBtn = driver.find_element_by_id("bmwradio")
        bmwRadioBtn.click()

        time.sleep(2)
        benzRadioBtn = driver.find_element_by_id("benzradio")
        benzRadioBtn.click()

        time.sleep(2)
        bmwCheckbox = driver.find_element_by_id("bmwcheck")
        bmwCheckbox.click()

        time.sleep(2)
        benzCheckbox = driver.find_element_by_id("benzcheck")
        benzCheckbox.click()

        print("BMW Radio button is selected? " + str(bmwRadioBtn.is_selected())) # True if selected, False is not selected
        print("Benz Radio button is selected? " + str(benzRadioBtn.is_selected()))
        print("BMW Checkbox is selected? " + str(bmwCheckbox.is_selected()))
        print("Benz Checkbox is selected? " + str(benzCheckbox.is_selected()))


        radio_btns_list=driver.find_elements(By.XPATH,'//fieldset//input[@type="radio"]')
        for i in range(len(radio_btns_list)):
            print(radio_btns_list[i].text)

        checkbox_list= driver.find_elements(By.XPATH,'//fieldset//input[@type="checkbox"]')
        for i in range(len(checkbox_list)):
            print(checkbox_list[i].text)

ff = RadioButtonsAndCheckboxes()
ff.test()
