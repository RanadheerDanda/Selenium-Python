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
            baseUrl='https://ksrtc.in/oprs-web/guest/home.do?h=1'
            driver = webdriver.Firefox(executable_path=path)
            driver.get(baseUrl)
            driver.maximize_window()
            driver.implicitly_wait(20)
            from_ = driver.find_element(By.XPATH,'//input[@id="fromPlaceName"]')
            from_.send_keys('Beng')
            time.sleep(2)
            from_.send_keys(Keys.ARROW_DOWN)
            print('print get text using driver method')
            print(from_.text)
            text1= 'BENGALURU AIRPORT'
            print('printing using js')
            script = "return document.getElementById(\"fromPlaceName\").value;";
            text = str(driver.execute_script(script))
            print(text)
            while text1 not in text:
                from_.send_keys(Keys.ARROW_DOWN)
                text = str(driver.execute_script(script))
            from_.send_keys(Keys.ENTER)








test=ExplicitWaitWithCalender()
test.explicit_wait_demo()