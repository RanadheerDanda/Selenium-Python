from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver import ActionChains
import time

class ExplicitWaitWithCalender:
        def explicit_wait_demo(self):
            path='F:\\selenium-java-3.141.59\\geckodriver.exe'
            baseUrl='https://www.expedia.co.in/'
            driver = webdriver.Firefox(executable_path=path)
            driver.get(baseUrl)
            driver.maximize_window()
            driver.implicitly_wait(5)
            flights_tab = driver.find_element(By.XPATH,'//button[@id="tab-flight-tab-hp"]')
            flights_tab.click()
            one_way = driver.find_element(By.XPATH,'//label[@id="flight-type-one-way-label-hp-flight"]')
            one_way.click()
            time.sleep(5)

            from_box = driver.find_element(By.XPATH,"//input[@id='flight-origin-hp-flight']")
            from_box.send_keys('Hyder')
            time.sleep(2)
            from_box.send_keys(Keys.ARROW_DOWN)
            print('print get text using driver method')
            print(from_box.text)
            text1 = 'Hyder, AK, United States of America (WHD)'
            print('printing using js')
            results = driver.find_elements(By.XPATH,'//ul[@id="typeaheadDataPlain"]//a[@class="details"]')

            #script = "return document.getElementById(\"flight-origin-hp-flight\").value;";
            #text = str(driver.execute_script(script))
            #print(text)
            for i in range(len(results)):
                print(results[i].__getattribute__('data-value'))
                compare = results[i].get_attribute('data-value')
                if text1 in compare:
                    break

            from_box.send_keys(Keys.ENTER)

            #Hyder, AK, United States of America (WHD) Hyder, AK, United States of America (WHD)





test=ExplicitWaitWithCalender()
test.explicit_wait_demo()