from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Test_Data import TC_PIMdata_06
import pytest
import time

class Test_PIM_Module:
    
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    
    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Firefox()
        yield 
        self.driver.close()
        
    def test_contact_details(self, booting_function):
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(3)
        # Login Functionality
        self.driver.find_element(by=By.NAME, value=TC_PIMdata_06.Selenium_Selectors.username_input).send_keys(TC_PIMdata_06.PIM_Data.username_data)
        self.driver.find_element(by=By.NAME, value=TC_PIMdata_06.Selenium_Selectors.password_input).send_keys(TC_PIMdata_06.PIM_Data.password_data)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_06.Selenium_Selectors.login_xpath).click()
        time.sleep(5)
        # Fill out all fields in contact details page on PIM module
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_06.Selenium_Selectors.PIM_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_06.Selenium_Selectors.employee_list_xpath).click()
        time.sleep(6)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_06.Selenium_Selectors.contact_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_06.Selenium_Selectors.street_xpath).send_keys(TC_PIMdata_06.PIM_Data.street_data)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_06.Selenium_Selectors.street_1_xpath).send_keys(TC_PIMdata_06.PIM_Data.street_1_data)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_06.Selenium_Selectors.city_xpath).send_keys(TC_PIMdata_06.PIM_Data.city_data)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_06.Selenium_Selectors.state_xpath).send_keys(TC_PIMdata_06.PIM_Data.state_data)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_06.Selenium_Selectors.postal_code_xpath).send_keys(TC_PIMdata_06.PIM_Data.postal_code_data)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_06.Selenium_Selectors.country_xpath).send_keys(Keys.DOWN, Keys.DOWN, Keys.ENTER)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_06.Selenium_Selectors.home_no_xpath).send_keys(TC_PIMdata_06.PIM_Data.home_no_data)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_06.Selenium_Selectors.mobile_no_xpath).send_keys(TC_PIMdata_06.PIM_Data.mobile_no_data)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_06.Selenium_Selectors.work_no_xpath).send_keys(TC_PIMdata_06.PIM_Data.work_no_data)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_06.Selenium_Selectors.email_xpath).send_keys(TC_PIMdata_06.PIM_Data.email_data)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_06.Selenium_Selectors.email_1_xpath).send_keys(TC_PIMdata_06.PIM_Data.email_1_data)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_06.Selenium_Selectors.save_1_xpath).click()
        time.sleep(8)
        # Validate the fields in contact details page on PIM module
        contact_details = self.driver.find_element(by=By.XPATH, value=TC_PIMdata_06.Selenium_Selectors.contact_1_xpath)
        contact_details.is_displayed()
        print("Status:",contact_details.is_displayed())
        print("Successfully all the filled details present in contact details page")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        