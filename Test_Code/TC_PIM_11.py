from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Test_Data import TC_PIMdata_11
import pytest
import time

class Test_PIM_Module:
    
    
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    
    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Firefox()
        yield 
        self.driver.close()
        
        
    def test_job_details(self, booting_function):
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(3)
        # Login Functionality
        self.driver.find_element(by=By.NAME, value=TC_PIMdata_11.Selenium_Selectors.username_input).send_keys(TC_PIMdata_11.PIM_Data.username_data)
        self.driver.find_element(by=By.NAME, value=TC_PIMdata_11.Selenium_Selectors.password_input).send_keys(TC_PIMdata_11.PIM_Data.password_data)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_11.Selenium_Selectors.login_xpath).click()
        time.sleep(5)
        # Fill out all the fields in employee job details page on PIM module
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_11.Selenium_Selectors.PIM_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_11.Selenium_Selectors.employee_list_xpath).click()
        time.sleep(6)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_11.Selenium_Selectors.job_xpath).click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_11.Selenium_Selectors.employement_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_11.Selenium_Selectors.Date_xpath).send_keys(TC_PIMdata_11.PIM_Data.date_data)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_11.Selenium_Selectors.dropdown_xpath).send_keys(Keys.DOWN, Keys.ENTER)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_11.Selenium_Selectors.reason_xpath).send_keys(TC_PIMdata_11.PIM_Data.reason_data)
        time.sleep(4)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_11.Selenium_Selectors.save_xpath).click()
        time.sleep(7)
        self.driver.refresh()
        time.sleep(4)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_11.Selenium_Selectors.employement_xpath).click()
        time.sleep(7)
        # Validate the activate employment in employee job details page
        active_employment = self.driver.find_element(by=By.XPATH, value=TC_PIMdata_11.Selenium_Selectors.employement1_xpath)
        active_employment.is_displayed()
        time.sleep(3)
        print("Status:",active_employment.is_displayed())
        print("Successfully activation on employee job details page") 
        
        
        
        
        