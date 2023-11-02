from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Test_Data import TC_PIMdata_08
import pytest
import time

class Test_PIM_Module:
    
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    
    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Firefox()
        yield 
        self.driver.close()
        
    def test_dependency_contact_details(self, booting_function):
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(3)
        # Login Functionality
        self.driver.find_element(by=By.NAME, value=TC_PIMdata_08.Selenium_Selectors.username_input).send_keys(TC_PIMdata_08.PIM_Data.username_data)
        self.driver.find_element(by=By.NAME, value=TC_PIMdata_08.Selenium_Selectors.password_input).send_keys(TC_PIMdata_08.PIM_Data.password_data)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_08.Selenium_Selectors.login_xpath).click()
        time.sleep(5)
        # Fill out all the fields in employee dependents contact details page on PIM module
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_08.Selenium_Selectors.PIM_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_08.Selenium_Selectors.employee_list_xpath).click()
        time.sleep(6)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_08.Selenium_Selectors.employee_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_08.Selenium_Selectors.add_xpath).click()
        time.sleep(4)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_08.Selenium_Selectors.name_xpath).send_keys(TC_PIMdata_08.PIM_Data.name_data)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_08.Selenium_Selectors.date_xpath).send_keys(TC_PIMdata_08.PIM_Data.date_data)
        time.sleep(3)
        a_relationship = self.driver.find_element(by=By.XPATH, value=TC_PIMdata_08.Selenium_Selectors.relationship_xpath)
        a_relationship.send_keys(Keys.DOWN, Keys.DOWN, Keys.ENTER)
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_08.Selenium_Selectors.specify_xpath).send_keys(TC_PIMdata_08.PIM_Data.specify_data)
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_08.Selenium_Selectors.save_1_xpath).click()
        time.sleep(7)
        # Validate the employee dependents contact details page
        dependency_details = self.driver.find_element(by=By.XPATH, value=TC_PIMdata_08.Selenium_Selectors.dependency_details)
        dependency_details.is_displayed()
        time.sleep(2)
        print("Status:",dependency_details.is_displayed())
        print("Successfully all the filled details present in employee dependents contact details page")
        
        
        