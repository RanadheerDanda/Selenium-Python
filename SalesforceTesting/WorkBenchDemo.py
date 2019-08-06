from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

class SalesforceDemo:
        def test_salesforce(self):
            path='F:\\selenium-java-3.141.59\\geckodriver.exe'
            baseUrl1 = 'https://workbench.developerforce.com/query.php'
            baseUrl='https://login.salesforce.com/'
            driver = webdriver.Firefox(executable_path=path)
            driver.implicitly_wait(20)
            driver.maximize_window()
            driver.get(baseUrl)
            username = driver.find_element(By.ID,"username")
            username.send_keys("drr.nani@gmail.com")
            password = driver.find_element(By.ID,"password")
            password.send_keys("Salesforce1!")
            login_button = driver.find_element(By.XPATH,"//input[@id='Login']")
            login_button.click()
            driver.get(baseUrl1)
            driver.find_element(By.XPATH, '//input[@id="termsAccepted"]').click()
            driver.find_element(By.ID, 'loginBtn').click()
            driver.find_element(By.XPATH,'//textarea[@id="soql_query_textarea"]').send_keys("select (SELECT Amount,ExpectedRevenue FROM Opportunities) from account where id ='0017F00001vDcxa'")
            query = driver.find_element(By.XPATH,"//input[@type='submit' and @name='querySubmit']")
            query.click()







test=SalesforceDemo()
test.test_salesforce()