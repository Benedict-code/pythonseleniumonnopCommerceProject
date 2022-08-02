import pytest
from selenium import webdriver
from pageObjects.LoginPageObject import *
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

#login test cases
class Test_001_Login:
    #Instead of hard coding the data, we use the config properites
    baseURL=ReadConfig.getApplicationURL()
    username=ReadConfig.getUserName()
    password=ReadConfig.getPassword()

    logger=LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homePageTitle(self,setup):
        self.logger.info("************** Test_001_Login ****************")
        self.logger.info("************** Verifying Home Page Title ****************")
        self.driver= setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        if act_title=="Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("************** Home Page title is passed ****************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.error("************** Home Page title is failed ****************")
            assert False

    @pytest.mark.sanity
    @pytest.mark.sanity
    def test_login(self,setup):
        self.logger.info("************** Verifying Login test ****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title2=self.driver.title
        if act_title2 =="Dashboard / nopCommerce administration":
            assert True
            self.logger.info("************** Login Test is passed ****************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.error("************** Login Test is failed ****************")
            assert False
