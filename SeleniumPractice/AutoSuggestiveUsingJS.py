from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import time

class AugtoSuggestiveDemo:
        def test_auto_suggestive(self):
            path='F:\\selenium-java-3.141.59\\geckodriver.exe'
            baseUrl='https://www.makemytrip.com/'
            driver = webdriver.Firefox(executable_path=path)
            driver.get(baseUrl)
            driver.maximize_window()
            driver.implicitly_wait(2)
            from_city = driver.find_element(By.XPATH,"//input[@id='fromCity']")
            driver.execute_script("arguments[0].value='';", from_city)
            driver.execute_script("arguments[0].value='Hyderabad';",from_city)
            time.sleep(2)

            # from_city = driver.find_element(By.XPATH,"//input[@type='text' and @placeholder='From']")
            #
            # #// *[ @ id = "react-autowhatever-1-section-1-item-2"]
            # from_city.send_keys('can')
            # time.sleep(5)
            #
            # for i in range(6):
            #     print(i)
            #     time.sleep(2)
            #     from_city.send_keys(Keys.ARROW_DOWN)
            # from_city.send_keys(Keys.ENTER)




test=AugtoSuggestiveDemo()
test.test_auto_suggestive()