from selenium import webdriver
from selenium.webdriver.common.by import  By

class SearchForCustomer:
    #Identify the locators
    srchbtn_xpath= "//div[@class='search-text']"  #"//div[@class='icon-search']//i[@class='fas fa-search']"
    txtemail_xpath="//input[@id='SearchEmail']"
    txtfname_xpath="//input[@id='SearchFirstName']"
    txtlname_xpath="//input[@id='SearchLastName']"
    btnsrch_xpath="//button[@id='search-customers']"
    table_xpath="//div[@class='row']//div[@class='col-md-12']//tbody"   #"//div[@class='dataTables_scroll']//tbody"
    tablerows_xpath="//div[@class='row']//div[@class='col-md-12']//tbody/tr"   #"//div[@class='dataTables_scroll']//tbody/tr"
    tablecolumns_xpath="//div[@class='row']//div[@class='col-md-12']//tbody/tr/td"   #"//div[@class='dataTables_scroll']//tbody/tr/td"
    #implement action methods for each locator
    def __init__(self, driver):  # gets the driver from the actual test case and...
        self.driver = driver
    def clicksrchicon(self):
        self.driver.find_element(By.XPATH,self.srchbtn_xpath).click()
    def enterSrchEmail(self,sEmail):
        self.driver.find_element(By.XPATH, self.txtemail_xpath).clear()
        self.driver.find_element(By.XPATH,self.txtemail_xpath).send_keys(sEmail)
    def enterSrchFName(self,fname):
        self.driver.find_element(By.XPATH, self.txtfname_xpath).clear()
        self.driver.find_element(By.XPATH,self.txtfname_xpath).send_keys(fname)
    def enterSrchLName(self,lname):
        self.driver.find_element(By.XPATH, self.txtlname_xpath).clear()
        self.driver.find_element(By.XPATH,self.txtlname_xpath).send_keys(lname)
    def clickSrchbtn(self):
        self.driver.find_element(By.XPATH,self.btnsrch_xpath).click()
    def getNoOfRows(self):
        return len(self.driver.find_elements(By.XPATH,self.tablerows_xpath))
    def getNoOfColumns(self):
        return len(self.driver.find_elements(By.XPATH, self.tablecolumns_xpath))
    def emailSrch(self,emailS):
        flag=False
        for r in range(1,self.getNoOfRows()+1):
            table=self.driver.find_element(By.XPATH,self.table_xpath)
            emailID=table.find_element(By.XPATH,"//div[@class='row']//div[@class='col-md-12']//tbody/tr["+str(r)+"]/td[2]")
            if emailID == emailS:
                flag=True
                break
        return flag
    def nameSrch(self,name):
        flag = False
        for r in range(1,self.getNoOfColumns()+1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            Name = table.find_element(By.XPATH, "//div[@class='row']//div[@class='col-md-12']//tbody/tr["+str(r)+"]/td[3]")
            if Name == name:
                flag = True
                break
        return flag