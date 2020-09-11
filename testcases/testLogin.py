import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig

from Utilities.customLogger import LogGen


class Test_001_Login:

    baseURL = ReadConfig.getApplicationURL()
    userName = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()



    def test_homePageTitle(self, setup):
        self.logger.info("*******************Test_001_Login************")
        self.logger.info("*******************verify home page title************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title

        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("*******************verify home page title passsed************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            assert False

    def test_login(self, setup):

        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.userName)
        self.lp.setPassword(self.password)
        self.lp.login()
        self.driver.title