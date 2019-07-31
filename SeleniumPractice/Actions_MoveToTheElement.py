from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class ActionsClass:
        def test_actions(self):
            path='F:\\selenium-java-3.141.59\\geckodriver.exe'
            baseUrl='http://www.qaclickacademy.com/practice.php'
            driver = webdriver.Firefox(executable_path=path)
            driver.get(baseUrl)
            driver.implicitly_wait(10)
            driver.execute_script('window:scrollBy(0,800);')
            time.sleep(3)
            driver.maximize_window()
            element =driver.find_element(By.XPATH,'//button[@id="mousehover"]')
            itemToClickLocator = '//div[@class="mouse-hover-content"]//a[text()="Top"]'
            try:
                actions = ActionChains(driver)
                actions.move_to_element(element).perform()
                print('Moved to the Mouse over')
                top =driver.find_element(By.XPATH,itemToClickLocator)
                actions.move_to_element(top).click().perform()
                print('item is clicked')
            except:
                print('Mouse over failed')






test=ActionsClass()
test.test_actions()