from selenium import webdriver

import time

class RunChromeTest:
    def run_chrome_test(self):

        driver = webdriver.Chrome('F:\\selenium-java-3.141.59\\chromedriver.exe')  # Optional argument, if not specified will search path.
        driver.get('http://www.google.com/xhtml');
        time.sleep(5)  # Let the user actually see something!
        search_box = driver.find_element_by_name('q')
        search_box.send_keys('ChromeDriver')
        search_box.submit()
        time.sleep(5)  # Let the user actually see something!
        #driver.quit()




cc=RunChromeTest()
cc.run_chrome_test()