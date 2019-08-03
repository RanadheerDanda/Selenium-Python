from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SalesforceDemo:
        def test_salesforce(self):
            path='F:\\selenium-java-3.141.59\\geckodriver.exe'
            baseUrl='https://login.salesforce.com/'
            driver = webdriver.Firefox(executable_path=path)
            driver.get(baseUrl)
            driver.implicitly_wait(20)
            driver.maximize_window()
            username = driver.find_element(By.ID,"username")
            username.send_keys("drr.nani@gmail.com")
            password = driver.find_element(By.ID,"password")
            password.send_keys("Salesforce1!")
            login_button = driver.find_element(By.XPATH,"//input[@id='Login']")
            login_button.click()
            driver.get('https://ap5.salesforce.com/0017F00001vDcxa')
            go_to_list = driver.find_element(By.XPATH,'//div[@id="0017F00001vDcxa_RelatedOpportunityList_body"]/div/a[2]')
            go_to_list.click()
            list_opty = driver.find_elements(By.XPATH,'//tr/td[2]//preceding::th[@scope="row"]//a')
            for i in range(len(list_opty)):
                list_opty1 = driver.find_elements(By.XPATH, '//tr/td[2]//preceding::th[@scope="row"]//a')
                list_opty1[i].click()
                edit = driver.find_element(By.XPATH, '//td[@id="topButtonRow"]/input[@name="edit"]')
                edit.click()
                stage_drpdwn = Select(driver.find_element(By.XPATH, '//select[@id="opp11"]'))
                stage_drpdwn.select_by_visible_text('Perception Analysis')
                save = driver.find_element(By.XPATH, '//td[@id="topButtonRow"]/input[@name="save"]')
                save.click()
                driver.back()
                time.sleep(3)
                driver.back()
                time.sleep(2)
                driver.back()
                time.sleep(2)






            driver.back()
            driver.refresh()













test=SalesforceDemo()
test.test_salesforce()