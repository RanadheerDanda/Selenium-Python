from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class ActionsClass:
        def test_actions(self):
            path='F:\\selenium-java-3.141.59\\geckodriver.exe'
            baseUrl='https://www.amazon.com/'
            driver = webdriver.Firefox(executable_path=path)
            driver.maximize_window()
            driver.get(baseUrl)
            driver.implicitly_wait(10)
            time.sleep(3)
            element =driver.find_element(By.XPATH,'//a[@id="nav-link-accountList"]')
            itemToClickLocator = '//a[@id=\"nav_prefetch_yourorders\"]/span'
            try:
                actions = ActionChains(driver)
                actions.move_to_element(element).perform()
                print('Moved to the Mouse over')
                time.sleep(5)
                top =driver.find_element(By.XPATH,itemToClickLocator)
                actions.move_to_element(top).click().perform()
                print('item is clicked')
            except:
                print('Mouse over failed')






test=ActionsClass()
test.test_actions()