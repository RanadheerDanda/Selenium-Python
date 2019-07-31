from selenium import webdriver


class RunFFTest:

     def test_method(self):
         #driver = webdriver.Chrome('F:\\selenium-java-3.141.59\\chromedriver.exe')
         driver =webdriver.Firefox(executable_path='F:\\selenium-java-3.141.59\\geckodriver.exe')
         driver.get('https://letskodeit.com')


ff=RunFFTest()
ff.test_method()
