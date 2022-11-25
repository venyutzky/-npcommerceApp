from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from npcommerceApp.pageObjects.LoginPage import LoginPage

class Test_001_Login:
    #Data preparation
    baseURL = "https://admin-demo.nopcommerce.com/"
    username = "admin@yourstore.com"
    password = "admin"

    def test_homePageTitlte(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login123":
            self.driver.close()
            assert True
            
        else:
            self.driver.get_screenshot_as_file(".\\npcommerceApp\\Screenshots\\test_homePageTitle.png")
            self.driver.close()
            assert False

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration123":
            self.driver.close()
            assert True
            
        else:
            self.driver.get_screenshot_as_file(".\\npcommerceApp\\Screenshots\\test_login.png")
            self.driver.close()
            assert False
    

