import pytest
from selenium import webdriver

from PageObjects import LoginPage

class Test_001_Login:
    baseURL  = "https://admin-demo.nopcommerce.com/"
    userName =  "admin@yourstore.com"
    password =  "admin"

    def test_homePageTitle(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title  = self.driver.title
        self.driver.close()
        if act_title=="Your store. Login":
            assert True
        else:
            assert False
    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage()
        self.lp.setUserName(self.userName)
        self.lp.setPassword(self.password)
        self.lp.login()
        self.driver.title