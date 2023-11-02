from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Test_Data import TC_PIMdata_03
import pytest
import time

class Test_PIM_Module:
    
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    
    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Firefox()
        yield 
        self.driver.close()
        
    def test_create_Employee(self, booting_function):
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(3)
        # Login functionality
        self.driver.find_element(by=By.NAME, value=TC_PIMdata_03.Selenium_Selectors.username_input).send_keys(TC_PIMdata_03.PIM_Data.username)
        self.driver.find_element(by=By.NAME, value=TC_PIMdata_03.Selenium_Selectors.password_input).send_keys(TC_PIMdata_03.PIM_Data.password)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_03.Selenium_Selectors.login_xpath).click()
        time.sleep(5)
        
        # Validate the creation of new employee on PIM module
        self.driver.find_element(by=By.LINK_TEXT, value=TC_PIMdata_03.Selenium_Selectors.PIM_text).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_03.Selenium_Selectors.add_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.NAME, value=TC_PIMdata_03.Selenium_Selectors.first_name).send_keys(TC_PIMdata_03.PIM_Data.firstname_data)
        self.driver.find_element(by=By.NAME, value=TC_PIMdata_03.Selenium_Selectors.middle_name).send_keys(TC_PIMdata_03.PIM_Data.middlename_data)
        self.driver.find_element(by=By.NAME, value=TC_PIMdata_03.Selenium_Selectors.last_name).send_keys(TC_PIMdata_03.PIM_Data.lastname_data)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_03.Selenium_Selectors.id_xpath).send_keys(TC_PIMdata_03.PIM_Data.id_data)
        time.sleep(4)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_03.Selenium_Selectors.create_button_xpath).click()
        time.sleep(4)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_03.Selenium_Selectors.username_xpath).send_keys(TC_PIMdata_03.PIM_Data.username_data)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_03.Selenium_Selectors.password_xpath).send_keys(TC_PIMdata_03.PIM_Data.password_data)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_03.Selenium_Selectors.conform_password_xpath).send_keys(TC_PIMdata_03.PIM_Data.conform_Password_data) 
        time.sleep(3)  
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_03.Selenium_Selectors.enabled_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_03.Selenium_Selectors.save_xpath).click()
        time.sleep(8)
        print("Successfully Employee List created")
        
        
        
        
        
        
        