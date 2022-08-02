import pytest
import time
from selenium import webdriver
from pageObjects.LoginPageObject import *
from pageObjects.addCustomerPageObject import AddCustomer
from pageObjects.srchCustomerbyEmailPageObject import SearchForCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_005_SrchCustomerByName:
    baseURL=ReadConfig.getApplicationURL()
    username=ReadConfig.getUserName()
    password=ReadConfig.getPassword()
    logger=LogGen.loggen()

    @pytest.mark.regression
    def test_srchCustomerByName(self,setup):
        self.logger.info("************ Test_005_SrchCustomerByName **************")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        lp=LoginPage(self.driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        self.logger.info("**********Login successful *************")

        sc=AddCustomer(self.driver)
        sc.clickCustomersMenu()
        sc.clickCustomeritemMenu()

        self.logger.info("***********Srch Customer By Name Started ************")
        search=SearchForCustomer(self.driver)
        #search.clicksrchicon()
        search.enterSrchFName("Victoria")
        search.enterSrchLName("Terces")
        search.clickSrchbtn()
        time.sleep(3)
        status=search.nameSrch("Victoria Terces")
        assert True==status
        self.logger.info("***********Srch Customer By Name Finished ************")
        driver.close()