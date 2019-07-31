from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class DragAndDrop:
        def test_drag_drop(self):
            path='F:\\selenium-java-3.141.59\\geckodriver.exe'
            baseUrl='https://jqueryui.com/droppable/'
            driver = webdriver.Firefox(executable_path=path)
            driver.maximize_window()
            driver.get(baseUrl)
            driver.implicitly_wait(10)
            driver.switch_to.frame(driver.find_elements(By.TAG_NAME,"iframe")[0])
            source_element = driver.find_element(By.ID,'draggable')
            target_element = driver.find_element(By.ID,'droppable')
            try:
                actions = ActionChains(driver)
                #actions.drag_and_drop(source_element,target_element).perform()
                #or
                actions.click_and_hold(source_element).move_to_element(target_element).release().perform()
                print('drag and drop is done')
                time.sleep(3)
                driver.quit()
            except:
                print('drag and drop is failed')









test=DragAndDrop()
test.test_drag_drop()