from selenium import webdriver

class Login:
    textbox_username_id="Email"
    textbox_password_id = "Password"
    button_login_xpath="//input[@class='button-1 login-button']"
    link_logout_linktext = "Logout"

    def __init__(self,driver):
        self.driver=driver

    def setUserName(self,userName):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(userName)

    def setPassword(self,password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)
    def login(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()