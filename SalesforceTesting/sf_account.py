from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from SalesforceTesting.Support.sf_locators import SFClssicLocators
import json
import yaml
import yamlordereddictloader

class SF_Accounts:
    def __init__(self):
        self.sf_locators = SFClssicLocators()
        yml_path = 'F:\PythonPractice\SalesforceTesting\config.yaml'
        with open(yml_path, 'r') as f:
            self.doc_yaml = yaml.load(f, Loader=yamlordereddictloader.Loader)
        pstr_filepath = "F:\\PythonPractice\\SalesforceTesting\\testdata\\sf_accounts.json"
        with open(pstr_filepath,'r') as config_yml:
            self.dataJson = json.load(config_yml)

        self.driver = webdriver.Firefox(executable_path=self.doc_yaml['driver_path'])
        self.driver.get(self.doc_yaml['base_url'])
        self.driver.implicitly_wait(self.doc_yaml['IMPLICIT_WAIT'])
        self.driver.maximize_window()


    def login_to_sf(self,username,password):

        self.driver.find_element(By.ID,self.sf_locators.str_user).send_keys(username)
        self.driver.find_element(By.ID,self.sf_locators.str_password).send_keys(password)
        self.driver.find_element(By.ID,self.sf_locators.str_submit).click()

    def navigate_to_account_tab(self):
        account_tab = self.driver.find_element(By.XPATH,str(self.sf_locators.str_tab).replace('<<text_replace>>','Account_Tab'))
        account_tab.click()
    def click_on_new_button(self):
        self.driver.find_element(By.XPATH,self.sf_locators.str_new_account_btn).click()

    def fill_account_inforamtion(self,pstr_environment,pstr_section,pstr_label=None,pdict_data={}):
        try:
            str_data_section = self.dataJson[pstr_environment][pstr_section]
            for field,data_type in str_data_section.items():
                print(field)
                print(data_type[0])
                print(data_type[1])
                if(data_type[1]=='input_field'):
                    self.driver.find_element(By.XPATH,str(self.sf_locators.str_common_input).replace('<<text_replace>>',field)).send_keys(data_type[0])
                elif(data_type[1]=='textarea'):
                    self.driver.find_element(By.XPATH,str(self.sf_locators.str_common_textarea).replace('<<text_replace>>',field)).send_keys(data_type[0])
                elif(data_type[1]=='dropdown'):
                    drpdwn=self.driver.find_element(By.XPATH,str(self.sf_locators.str_common_dropdown).replace('<<text_replace>>',field))
                    select = Select(drpdwn)
                    select.select_by_visible_text(data_type[0])
                # elif(data_type[1]=='lookup'):
                #     window_before = self.driver.current_window_handle
                #     self.driver.find_element(By.XPATH,str(self.sf_locators.str_lookup_icon).replace('<<text_replace>>',field)).click()
                #     window_after = self.driver.window_handles[1]
                #     self.driver.switch_to.window(window_after)
                #     self.driver.switch_to.frame('resultsFrame')
                #     self.driver.find_element(By.PARTIAL_LINK_TEXT, data_type[0]).click()
                #     time.sleep(2)
                #     self.driver.switch_to(window_before)

                else:
                    pass

        except Exception as e:
            print(e)

    def click_save_button(self,action):
        self.driver.find_element(By.XPATH,str(self.sf_locators.str_header_buttons).replace('<<text_replace>>',action)).click()

    def get_accout_data(self):
        #print(self.dataJson)
        self.fill_account_inforamtion('create_account_data','Account Information')

test = SF_Accounts()
test.login_to_sf(username=test.doc_yaml['username'],password=test.doc_yaml['password'])
test.navigate_to_account_tab()
test.click_on_new_button()
test.fill_account_inforamtion('create_account_data','Account Information')
test.click_save_button('Save')







