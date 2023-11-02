from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Test_Data import TC_PIMdata_05
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
        self.driver.find_element(by=By.NAME, value=TC_PIMdata_05.Selenium_Selectors.username_input).send_keys(TC_PIMdata_05.PIM_Data.username)
        self.driver.find_element(by=By.NAME, value=TC_PIMdata_05.Selenium_Selectors.password_input).send_keys(TC_PIMdata_05.PIM_Data.password)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_05.Selenium_Selectors.login_xpath).click()
        time.sleep(5)
        
        # Fill out all the fields in personal details page
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_05.Selenium_Selectors.PIM_xpath).click()
        time.sleep(3)
        self.driver.execute_script("window.scrollBy(0,500)","")
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_05.Selenium_Selectors.employee_list_xpath).click()
        time.sleep(7)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_05.Selenium_Selectors.id_xpath).send_keys(TC_PIMdata_05.PIM_Data.id_no)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_05.Selenium_Selectors.license_xpath).send_keys(TC_PIMdata_05.PIM_Data.license_no)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_05.Selenium_Selectors.expiry_xpath).send_keys(TC_PIMdata_05.PIM_Data.license_date)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_05.Selenium_Selectors.SSN_xpath).send_keys(TC_PIMdata_05.PIM_Data.SSN_no)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_05.Selenium_Selectors.SIN_xpath).send_keys(TC_PIMdata_05.PIM_Data.SIN_no)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_05.Selenium_Selectors.nationality_xpath).send_keys(Keys.DOWN, Keys.DOWN, Keys.ENTER)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_05.Selenium_Selectors.marital_xpath).send_keys(Keys.DOWN, Keys.ENTER)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_05.Selenium_Selectors.DOB_xpath).send_keys(TC_PIMdata_05.PIM_Data.DOB)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_05.Selenium_Selectors.male_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_05.Selenium_Selectors.save_xpath).click()
        time.sleep(6)
        # Validate the personal details in employee list page on PIM module
        self.driver.execute_script("window.scrollBy(0,-1000)","")
        time.sleep(6)
        self.driver.execute_script("window.scrollBy(0,600)","")
        time.sleep(2)
        personal_details = self.driver.find_element(by=By.XPATH, value=TC_PIMdata_05.Selenium_Selectors.personal_details_page)
        personal_details.is_displayed()
        time.sleep(3)
        print("Status:",personal_details.is_displayed())
        print("Successfully all the filled details persent in personal details page")
        
        
        
        
        
        
      
        
        
        
        
        
        
        
        
        
        
        