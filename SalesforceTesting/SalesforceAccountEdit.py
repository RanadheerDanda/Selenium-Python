from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

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
            Parent_handle = driver.current_window_handle
            edit_account = driver.find_element(By.XPATH,'//td[@id="topButtonRow"]/input[@name="edit"]')
            edit_account.click()
            parent_account = driver.find_element(By.XPATH,'//input[@id="acc3"]')
            parent_account.clear()
            parent_account.send_keys('Test')
            lookup_button = driver.find_element(By.XPATH,'//a[@id="acc3_lkwgt"]/img')
            lookup_button.click()
            time.sleep(5)
            handles = driver.window_handles
            for handle in handles:
                if handle not in Parent_handle:
                    driver.switch_to.window(handle)
                    driver.switch_to.frame('resultsFrame')
                    driver.find_element(By.PARTIAL_LINK_TEXT,'Test Account2').click()
                    #driver.close()
            driver.switch_to.window(Parent_handle)
            #SLA =driver.find_element(By.XPATH,'//label[text()="SLA Expiration Date"]//following::input')
            #SLA.send_keys('7/31/2019')
            #SLA.click()
            #Calender = driver.find_element(By.XPATH,'//div[@id="datePicker"]//tr[@id="calRow5"]/td[text()="2"]')
            #Calender.click()
            save_btn = driver.find_element(By.XPATH,'//td[@id="bottomButtonRow"]/input[@name="save"]')
            save_btn.click()
            Opportunity_list = driver.find_elements(By.XPATH,'//div[@id="0017F00001vDcxa_RelatedOpportunityList"]/div[contains(@class,"opportunityBlock")]//th[@scope="row"]//a')
            for opty in Opportunity_list:
                opty.send_keys(Keys.CONTROL,Keys.ENTER)








test=SalesforceDemo()
test.test_salesforce()