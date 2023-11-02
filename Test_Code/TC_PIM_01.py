from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from Test_Data import TC_PIMdata_01
import pytest
import time

class Test_Admin_Page:
    
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    
    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Firefox()
        yield 
        self.driver.close()
        
        
    def test_admin(self, booting_function):
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(4)
        # Login Functionality
        self.driver.find_element(by=By.NAME, value=TC_PIMdata_01.Selenium_Selectors.username_input).send_keys(TC_PIMdata_01.PIM_Data.username)
        self.driver.find_element(by=By.NAME, value=TC_PIMdata_01.Selenium_Selectors.password_input).send_keys(TC_PIMdata_01.PIM_Data.password)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_01.Selenium_Selectors.login_xpath).click()
        time.sleep(5)
        print("Successfully Login")
        
        # Validate the Admin page menu options
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_01.Selenium_Selectors.admin_xpath).click()
        time.sleep(3)
        menu_options = self.driver.find_element(by=By.XPATH, value=TC_PIMdata_01.Selenium_Selectors.search_xpath)
        action = ActionChains(self.driver)
        action.click(on_element=menu_options).send_keys('pim').perform()
        time.sleep(5)
        self.driver.find_element(by=By.LINK_TEXT, value=TC_PIMdata_01.Selenium_Selectors.PIM_text).click()
        time.sleep(3)
        menu_options = self.driver.find_element(by=By.XPATH, value=TC_PIMdata_01.Selenium_Selectors.search_xpath)
        action = ActionChains(self.driver)
        action.click(on_element=menu_options).send_keys('leave').perform()
        time.sleep(5)
        self.driver.find_element(by=By.LINK_TEXT, value=TC_PIMdata_01.Selenium_Selectors.leave_text).click()
        time.sleep(3)
        menu_options = self.driver.find_element(by=By.XPATH, value=TC_PIMdata_01.Selenium_Selectors.search_xpath)
        action = ActionChains(self.driver)
        action.click(on_element=menu_options).send_keys('time').perform()
        time.sleep(5)
        self.driver.find_element(by=By.LINK_TEXT, value=TC_PIMdata_01.Selenium_Selectors.time_text).click()
        time.sleep(3)
        menu_options = self.driver.find_element(by=By.XPATH, value=TC_PIMdata_01.Selenium_Selectors.search_xpath)
        action = ActionChains(self.driver)
        action.click(on_element=menu_options).send_keys('recruitment').perform()
        time.sleep(5)
        self.driver.find_element(by=By.LINK_TEXT, value=TC_PIMdata_01.Selenium_Selectors.recruitment_text).click()
        time.sleep(3)
        menu_options = self.driver.find_element(by=By.XPATH, value=TC_PIMdata_01.Selenium_Selectors.search_xpath)
        action = ActionChains(self.driver)
        action.click(on_element=menu_options).send_keys('my info').perform()
        time.sleep(5)
        self.driver.find_element(by=By.LINK_TEXT, value=TC_PIMdata_01.Selenium_Selectors.myinfo_text).click()
        time.sleep(3)
        menu_options = self.driver.find_element(by=By.XPATH, value=TC_PIMdata_01.Selenium_Selectors.search_xpath)
        action = ActionChains(self.driver)
        action.click(on_element=menu_options).send_keys('performance').perform()
        time.sleep(5)
        self.driver.find_element(by=By.LINK_TEXT, value=TC_PIMdata_01.Selenium_Selectors.performance_text).click()
        time.sleep(3)
        menu_options = self.driver.find_element(by=By.XPATH, value=TC_PIMdata_01.Selenium_Selectors.search_xpath)
        action = ActionChains(self.driver)
        action.click(on_element=menu_options).send_keys('dashboard').perform()
        time.sleep(5)
        self.driver.find_element(by=By.LINK_TEXT, value=TC_PIMdata_01.Selenium_Selectors.dashboard_text).click()
        time.sleep(3)
        menu_options = self.driver.find_element(by=By.XPATH, value=TC_PIMdata_01.Selenium_Selectors.search_xpath)
        action = ActionChains(self.driver)
        action.click(on_element=menu_options).send_keys('directory').perform()
        time.sleep(5)
        self.driver.find_element(by=By.LINK_TEXT, value=TC_PIMdata_01.Selenium_Selectors.directory_text).click()
        time.sleep(3)
        menu_options = self.driver.find_element(by=By.XPATH, value=TC_PIMdata_01.Selenium_Selectors.search_xpath)
        action = ActionChains(self.driver)
        action.click(on_element=menu_options).send_keys('maintenance').perform()
        time.sleep(5)
        self.driver.find_element(by=By.LINK_TEXT, value=TC_PIMdata_01.Selenium_Selectors.maintenance_text).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_01.Selenium_Selectors.cancel_button).click()
        time.sleep(3)
        menu_options = self.driver.find_element(by=By.XPATH, value=TC_PIMdata_01.Selenium_Selectors.search_xpath)
        action = ActionChains(self.driver)
        action.click(on_element=menu_options).send_keys('buzz').perform()
        time.sleep(3)
        self.driver.find_element(by=By.LINK_TEXT, value=TC_PIMdata_01.Selenium_Selectors.buzz_text).click()
        time.sleep(5)
        menu_options = self.driver.find_element(by=By.XPATH, value=TC_PIMdata_01.Selenium_Selectors.search_xpath)
        menu_options.is_displayed()
        print("status:",menu_options.is_displayed())
        print("Successfully displayed on menu options")
        time.sleep(6)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            
            
        
        
        
        
        
        
        
        
           