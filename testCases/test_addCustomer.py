import pytest
import time
import string
import random
from selenium import webdriver
from pageObjects.LoginPageObject import *
from pageObjects.addCustomerPageObject import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression  #U need to group your test cases before starting automation testing
    def test_addCustomer(self,setup):
        self.logger.info("*********** Test_003_AddCustomer *************")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("******** Login successful **********")

        self.logger.info("******** Starting Add Customer Test **********")
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickCustomersMenu()
        self.addcust.clickCustomeritemMenu()
        self.addcust.clickAddNew()
        self.logger.info("******* Providing customer info ********")
        self.email = random_generator() + "@gmail.com"
        self.addcust.enterEmail(self.email)
        self.addcust.enterPasswd("test123")
        self.addcust.enterFname("Carson")
        self.addcust.enterLname("Carsonn")
        self.addcust.selectGender("Male")
        self.addcust.enterDOB("7/05/2000")
        self.addcust.enterCompname("JTex")
        self.addcust.selectChekbox1()
        self.addcust.clickNewsL()
        self.addcust.selectStore("Test store 2")
        self.addcust.setCustomerRoles("Registered")
        self.addcust.selectMVendors("Vendor 2")
        self.addcust.enterComment("Adding new customer...")
        self.addcust.clickSave()

        self.logger.info("******* Saving Customer Info **********")
        self.logger.info("*********** Add Customer Validation Started ************")
        self.msg = self.driver.find_element(By.TAG_NAME,"body").text
        print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            assert True ==True
            self.logger.info("*********Add customer Test Passed **********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")
            self.logger.error("********** Add Customer Test Failed *********")
            assert True == False

        self.driver.close()
        self.logger.info("*********** Ending Test_003_AddCustomer Test")

def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
