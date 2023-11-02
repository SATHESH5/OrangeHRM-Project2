from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Test_Data import TC_PIMdata_04
import pytest
import time

class Test_PIM_Module:
    
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    
    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Firefox()
        yield 
        self.driver.close()
        
    def test_Employee_Details(self, booting_function):
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(3)
        # Login functionality
        self.driver.find_element(by=By.NAME, value=TC_PIMdata_04.Selenium_Selectors.username_input).send_keys(TC_PIMdata_04.PIM_Data.username)
        self.driver.find_element(by=By.NAME, value=TC_PIMdata_04.Selenium_Selectors.password_input).send_keys(TC_PIMdata_04.PIM_Data.password)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_04.Selenium_Selectors.login_xpath).click()
        time.sleep(5)
        
        # Validate the employee list details on PIM module
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_04.Selenium_Selectors.PIM_xpath).click()
        time.sleep(3)
        self.driver.execute_script("window.scrollBy(0,1000)","")
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_04.Selenium_Selectors.employee_list_xpath).click()
        time.sleep(7)
        employee_list_page = self.driver.find_element(by=By.XPATH, value=TC_PIMdata_04.Selenium_Selectors.employee_xpath)
        time.sleep(3)
        self.driver.execute_script("window.scrollBy(0,600)","")
        employee_list_page.is_displayed()
        time.sleep(4)
        print("status:", employee_list_page.is_displayed())
        print("Successfully all the tabs present in employee list page")
        
        
        
        
        
        
        