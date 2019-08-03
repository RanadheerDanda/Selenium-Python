from selenium import webdriver
from selenium.webdriver.common.by import By
import time
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
            all_tabs = driver.find_element(By.XPATH,'//li[@id="AllTab_Tab"]/a/img')
            all_tabs.click()
            lead_link = driver.find_element(By.PARTIAL_LINK_TEXT,'Leads')
            lead_link.click()
            new_lead = driver.find_element(By.XPATH,'//td[@class="pbButton"]//input')
            new_lead.click()
            last_name = driver.find_element(By.XPATH,'//*[@id="name_lastlea2"]')
            last_name.send_keys('Test Ranadheer')
            company_name = driver.find_element(By.XPATH,'//label[@for="lea3"]//following::input')
            company_name.send_keys('Test Cognizant51')
            lead_status = driver.find_element(By.XPATH,'//label[contains(text(),"Lead Status")]//following::select[@name="lea13"]')
            lead_status_dropdown = Select(lead_status)
            lead_status_dropdown.select_by_visible_text('Working - Contacted')
            save_btn = driver.find_element(By.XPATH,'//td[@id="topButtonRow"]/input[@name="save"]')
            save_btn.click()
            time.sleep(3)
            str_record_link = driver.current_url
            print(str_record_link)
            convert_btn = driver.find_element(By.XPATH,'//td[@id="topButtonRow"]/input[@value="Convert"]')
            convert_btn.click()
            account_name = driver.find_element(By.XPATH,'//select[@id="accid"]')
            account_name_drpdwn = Select(account_name)
            account_name_drpdwn.select_by_visible_text('Create New Account: Test Cognizant51')
            opportunity_name = driver.find_element(By.XPATH,'//input[@id="noopptt"]')
            opportunity_name.clear()
            opportunity_name.send_keys('Test Cognizant51')
            convert = driver.find_element(By.XPATH,'//*[@id="topButtonRow"]/input[@name="save"]')
            convert.click()








test=SalesforceDemo()
test.test_salesforce()