import pytest
import time
from selenium import webdriver
from pageObjects.LoginPageObject import *
from pageObjects.addCustomerPageObject import AddCustomer
from pageObjects.srchCustomerbyEmailPageObject import SearchForCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_004_SrchCustomerByEmail:
    baseURL=ReadConfig.getApplicationURL()
    username=ReadConfig.getUserName()
    password=ReadConfig.getPassword()
    logger=LogGen.loggen()

    @pytest.mark.regression
    def test_srchCustomer(self,setup):
        self.logger.info("************ Test_004_SrchCustomer **************")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("**********Login successful *************")

        self.sc=AddCustomer(self.driver)
        self.sc.clickCustomersMenu()
        self.sc.clickCustomeritemMenu()

        self.logger.info("***********Srch Customer By Email Started ************")

        self.search=SearchForCustomer(self.driver)

        #self.search.clicksrchicon()
        self.search.enterSrchEmail("admin@yourStore.com")
        self.search.clickSrchbtn()
        time.sleep(3)
        status=self.search.emailSrch("admin@yourStore.com")
        assert True==status
        self.logger.info("***********Srch Customer By Email Finished ************")
        self.driver.close()