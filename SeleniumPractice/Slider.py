from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class SliderExample:
        def slider_test(self):
            path='F:\\selenium-java-3.141.59\\geckodriver.exe'
            baseUrl='https://jqueryui.com/slider/'
            driver = webdriver.Firefox(executable_path=path)
            driver.maximize_window()
            driver.get(baseUrl)
            driver.implicitly_wait(10)
            driver.switch_to.frame(driver.find_elements_by_tag_name('iframe')[0])
            slider_element = driver.find_element(By.XPATH,'//div[@id="slider"]//span')

            try:
                actions = ActionChains(driver)
                print('sliding in right direction')
                actions.drag_and_drop_by_offset(slider_element,500,0).perform()
                time.sleep(5)

            except:
                print('sliding is failed')
            finally:
                driver.quit()










test=SliderExample()
test.slider_test()