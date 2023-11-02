from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Test_Data import TC_PIMdata_13
import pytest
import time

class Test_PIM_Module:
    
    
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    
    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Firefox()
        yield 
        self.driver.close()
        
        
    def test_employee_tax_details(self, booting_function):
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(3)
        # Login Functionality
        self.driver.find_element(by=By.NAME, value=TC_PIMdata_13.Selenium_Selectors.username_input).send_keys(TC_PIMdata_13.PIM_Data.username_data)
        self.driver.find_element(by=By.NAME, value=TC_PIMdata_13.Selenium_Selectors.password_input).send_keys(TC_PIMdata_13.PIM_Data.password_data)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_13.Selenium_Selectors.login_xpath).click()
        time.sleep(5)
        # Fill out all the fields in employee tax exemptions details page on PIM module
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_13.Selenium_Selectors.PIM_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_13.Selenium_Selectors.employee_list_xpath).click()
        time.sleep(6)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_13.Selenium_Selectors.tax_xpath).click()
        time.sleep(5)
        status_role = self.driver.find_element(by=By.XPATH, value=TC_PIMdata_13.Selenium_Selectors.status_xpath).send_keys(Keys.DOWN, Keys.DOWN, Keys.ENTER)
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_13.Selenium_Selectors.exemptions_xpath).send_keys(TC_PIMdata_13.PIM_Data.exemptions_data)
        time.sleep(2)
        state_role = self.driver.find_element(by=By.XPATH, value=TC_PIMdata_13.Selenium_Selectors.state_xpath).send_keys(Keys.DOWN, Keys.DOWN, Keys.ENTER)
        time.sleep(2)
        status_1_role = self.driver.find_element(by=By.XPATH, value=TC_PIMdata_13.Selenium_Selectors.status_1_xpath).send_keys(Keys.DOWN, Keys.DOWN, Keys.ENTER)
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_13.Selenium_Selectors.exemptions_1_xpath).send_keys(TC_PIMdata_13.PIM_Data.exemptions_1_data)
        time.sleep(3)
        unemployment_state = self.driver.find_element(by=By.XPATH, value=TC_PIMdata_13.Selenium_Selectors.unemployment_xpath).send_keys(Keys.DOWN, Keys.DOWN, Keys.DOWN, Keys.ENTER)
        time.sleep(2)
        work_state = self.driver.find_element(by=By.XPATH, value=TC_PIMdata_13.Selenium_Selectors.work_xpath).send_keys(Keys.DOWN, Keys.DOWN, Keys.ENTER)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_13.Selenium_Selectors.save_1_xpath).click()
        time.sleep(5)
        employee_tax = self.driver.find_element(by=By.XPATH, value=TC_PIMdata_13.Selenium_Selectors.tax_exemptions)
        employee_tax.is_displayed()
        time.sleep(2)
        print("Status:",employee_tax.is_displayed())
        print("Successfully updating employee salary on tax exemptions page")
        
        
        
        
        
        
        
        
        
        