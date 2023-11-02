from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Test_Data import TC_PIMdata_07
import pytest
import time

class Test_PIM_Module:
    
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    
    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Firefox()
        yield 
        self.driver.close()
        
    
    def test_emergency_contact_details(self, booting_function):
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(3)
        # Login Functionality
        self.driver.find_element(by=By.NAME, value=TC_PIMdata_07.Selenium_Selectors.username_input).send_keys(TC_PIMdata_07.PIM_Data.username_data)
        self.driver.find_element(by=By.NAME, value=TC_PIMdata_07.Selenium_Selectors.password_input).send_keys(TC_PIMdata_07.PIM_Data.password_data)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_07.Selenium_Selectors.login_xpath).click()
        time.sleep(5)
        # Fill out all the fields in emergency contact page on PIM module
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_07.Selenium_Selectors.PIM_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_07.Selenium_Selectors.employee_list_xpath).click()
        time.sleep(6)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_07.Selenium_Selectors.contact_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_07.Selenium_Selectors.add_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_07.Selenium_Selectors.name_xpath).send_keys(TC_PIMdata_07.PIM_Data.name_data)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_07.Selenium_Selectors.relationship_xpath).send_keys(TC_PIMdata_07.PIM_Data.relationship_data)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_07.Selenium_Selectors.home_no_xpath).send_keys(TC_PIMdata_07.PIM_Data.home_no_data)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_07.Selenium_Selectors.mobile_no_xpath).send_keys(TC_PIMdata_07.PIM_Data.mobile_no_data)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_07.Selenium_Selectors.work_no_xpath).send_keys(TC_PIMdata_07.PIM_Data.work_no_data)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_07.Selenium_Selectors.save_1_xpath).click()
        time.sleep(8)
        Emergency_Contact_Details = self.driver.find_element(by=By.XPATH, value=TC_PIMdata_07.Selenium_Selectors.emergency_contact_xpath)
        Emergency_Contact_Details.is_displayed()
        time.sleep(2)
        print("Status:",Emergency_Contact_Details.is_displayed())
        print("Successfully all the details present in emergency contact details page")
        
       
       
        
        