from selenium.webdriver.common.by import By

class LoginPage():
    def __init__(self,driver):
        self.driver = driver
        self.user_name_text_box_xpath = '//input[@id="username"]'
        self.password_text_box_xpath = '//input[@placeholder="Password"]'
        self.submit_button_xpath = '//button[@type="submit"]' 


    def enter_username(self,username):
        self.driver.find_element(By.XPATH,self.user_name_text_box_xpath).clear
        self.driver.find_element(By.XPATH,self.user_name_text_box_xpath).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element(By.XPATH,self.password_text_box_xpath).clear
        self.driver.find_element(By.XPATH,self.password_text_box_xpath).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH,self.submit_button_xpath).click()