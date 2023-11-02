from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Test_Data import TC_PIMdata_12
import pytest
import time

class Test_PIM_Module:
    
    
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    
    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Firefox()
        yield 
        self.driver.close()
        
        
    def test_emplyee_salary_details(self, booting_function):
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(3)
        # Login Functionality
        self.driver.find_element(by=By.NAME, value=TC_PIMdata_12.Selenium_Selectors.username_input).send_keys(TC_PIMdata_12.PIM_Data.username_data)
        self.driver.find_element(by=By.NAME, value=TC_PIMdata_12.Selenium_Selectors.password_input).send_keys(TC_PIMdata_12.PIM_Data.password_data)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_12.Selenium_Selectors.login_xpath).click()
        time.sleep(5)
        # Fill out all the fields in employee salary details page on PIM module
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_12.Selenium_Selectors.PIM_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_12.Selenium_Selectors.employee_list_xpath).click()
        time.sleep(6)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_12.Selenium_Selectors.salary_xpath).click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_12.Selenium_Selectors.add_1_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_12.Selenium_Selectors.component_xpath).send_keys(TC_PIMdata_12.PIM_Data.salary_data)
        pay_grade = self.driver.find_element(by=By.XPATH, value=TC_PIMdata_12.Selenium_Selectors.grade_xpath)
        pay_grade.send_keys(Keys.DOWN)
        pay_grade.click()
        time.sleep(2)
        pay_frequency = self.driver.find_element(by=By.XPATH, value=TC_PIMdata_12.Selenium_Selectors.frequency_xpath).send_keys(Keys.DOWN, Keys.DOWN, Keys.DOWN, Keys.ENTER)
        time.sleep(3)
        currency_amount = self.driver.find_element(by=By.XPATH, value=TC_PIMdata_12.Selenium_Selectors.currency_xpath)
        currency_amount.send_keys('Ecuador Sucre')
        currency_amount.send_keys(Keys.ENTER)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_12.Selenium_Selectors.amount_xpath).send_keys(TC_PIMdata_12.PIM_Data.amount_data)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_12.Selenium_Selectors.comment_xpath).send_keys(TC_PIMdata_12.PIM_Data.comment_data)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_12.Selenium_Selectors.click_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_12.Selenium_Selectors.account_no_xpath).send_keys(TC_PIMdata_12.PIM_Data.Account_No_data)
        time.sleep(2)
        account_type = self.driver.find_element(by=By.XPATH, value=TC_PIMdata_12.Selenium_Selectors.account_xpath)
        time.sleep(2)
        account_type.send_keys(Keys.DOWN, Keys.DOWN, Keys.DOWN, Keys.ENTER)
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_12.Selenium_Selectors.specify_xpath).send_keys(TC_PIMdata_12.PIM_Data.specify_data)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_12.Selenium_Selectors.routing_xpath).send_keys(TC_PIMdata_12.PIM_Data.routing_data)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_12.Selenium_Selectors.amount_1_xpath).send_keys(TC_PIMdata_12.PIM_Data.amount_1_data)
        time.sleep(4)
        self.driver.execute_script("window.scrollTo(0,100)")
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_12.Selenium_Selectors.save_1_xpath).click()
        time.sleep(8)
        # validate the filled filelds in employee salary details page
        salary_details = self.driver.find_element(by=By.XPATH, value=TC_PIMdata_12.Selenium_Selectors.salary_xpath_1)
        salary_details.is_displayed()
        time.sleep(2)
        print("Status:",salary_details.is_displayed())
        print("Successfully updating employee salary details page")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        