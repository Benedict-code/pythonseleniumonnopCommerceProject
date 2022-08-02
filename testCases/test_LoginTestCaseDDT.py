import pytest
from selenium import webdriver
from pageObjects.LoginPageObject import *
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import ExcelUtilityFunctions
import time

#login test cases
class Test_001_DDT_Login:
    #Instead of hard coding the data, we use the config properites
    baseURL=ReadConfig.getApplicationURL()
    path=".//testData/DDT_pytest_python.xlsx"

    logger=LogGen.loggen()

    @pytest.mark.sanity
    def test_DDT(self,setup):
        self.logger.info("************* Test_001_DDT_Login ******************")
        self.logger.info("************** Verifying Login test ****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        #DATA FROM THE EXCEL FILE
        self.rows=ExcelUtilityFunctions.getRowCount(self.path,"Sheet1")
        print("Number of Rows in Excel:", self.rows)

        list_status=[]  #Empty list variable

        for r in range(2,self.rows+1):
            self.user=ExcelUtilityFunctions.readData(self.path,"Sheet1",r,1)
            self.password=ExcelUtilityFunctions.readData(self.path,"Sheet1",r,2)
            self.exp=ExcelUtilityFunctions.readData(self.path,"Sheet1",r,3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)
            act_title2=self.driver.title
            exp_title="Dashboard / nopCommerce administration"
            if act_title2==exp_title:
                if self.exp=="Pass":
                    print("Test got passed")
                    self.logger.info("*** Passed ***")
                    self.lp.clickLogout()
                    list_status.append("Pass")
                elif self.exp=="Fail":
                    print("Test got failed")
                    self.logger.info("*** failed ***")
                    self.lp.clickLogout()
                    list_status.append("Fail")
            elif act_title2 != exp_title:
                if self.exp =="Pass":
                    print('Test got failed')
                    self.logger.info("*** failed ***")
                    list_status.append("Fail")
                elif self.exp == "Fail":
                    print("Test got passed")
                    self.logger.info("*** passed ***")
                    list_status.append("Pass")
        if "Fail" not in list_status:
            print("DDT Login test got passed")
            self.logger.info("*** Login DDT test passed... ***")
            self.driver.close()
            assert True
        else:
            print("DDT Login test got failed")
            self.logger.info("*** Login DDT test failed... ***")
            self.driver.close()
            assert False

        self.logger.info("************** End of Login DDT Test ****************")
        self.logger.info("************** Completed TC_LoginDDT_002 ****************")


