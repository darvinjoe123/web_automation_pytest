from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pytest
import allure
import moment
from pages.loginPage import LoginPage
from pages.homePage import HomePage
from utils import utils as utils
import os



@pytest.mark.usefixtures("test_setup")
class Testlogin():
    def test_login(self):
        driver=self.driver 
        driver.get(utils.URL)
        time.sleep(5)
        login = LoginPage(driver)
        login.enter_username(utils.USERNAME)
        login.enter_password(utils.PASSWORD)
        screenshot_name=f'{utils.whoami()}_{moment.now().strftime("%y-%m-%d_%H-%M-%S")}'
        allure.attach(driver.get_screenshot_as_png(),name=screenshot_name,attachment_type=allure.attachment_type.PNG)
        driver.get_screenshot_as_file('D:/web_automation/sample_automation_test/screenshots/'+screenshot_name+'.png')
        time.sleep(5)
        login.click_login()
        time.sleep(5)

    def test_notification(self):
        driver=self.driver 
        home=HomePage(driver)
        home.click_notification()
        time.sleep(3)

    def test_logout(self):
        driver=self.driver 
        home=HomePage(driver)
        home.click_logout
        screenshot_name=f'{utils.whoami()}_{moment.now().strftime("%y-%m-%d_%H-%M-%S")}'
        allure.attach(driver.get_screenshot_as_png(),name=screenshot_name,attachment_type=allure.attachment_type.PNG)
        driver.get_screenshot_as_file('D:/web_automation/sample_automation_test/screenshots/'+screenshot_name+'.png')


