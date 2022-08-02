import time
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By

class AddCustomer:
    #Identify the locators
    lnk_cust_menu_xpath="//a[@href='#']//p[contains(text(),'Customers')]"
    lnk_cust_menuitem_xpath="//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btnAddnew_xpath="//a[normalize-space()='Add new']"
    txtEmail_xpath="//input[@id='Email']"
    txtPass_xpath="//input[@id='Password']"
    txtFname_xpath="//input[@id='FirstName']"
    txtLname_xpath="//input[@id='LastName']"
    rdmale_xpath="//input[@id='Gender_Male']"
    rdFmale_xpath="//input[@id='Gender_Female']"
    txtDOB_xpath="//input[@id='DateOfBirth']"
    txtComName_xpath="//input[@id='Company']"
    chekbox1_xpath="//input[@id='IsTaxExempt']"
    txtNews_xpath="//div[@class='k-multiselect-wrap k-floatwrap']"
    lstStorname_xpath="//li[text()='Your store name']"
    lstTestStore_xpath="//li[text()='Test store 2']"
    lstCustRoles_xpath='//*[@id="customer-info"]/div[2]/div[10]/div[2]/div/div[1]/div/div'       #"//input[@aria-expanded='true']"
    lstitemAdm_xpath="//li[text()='Administrators']"
    lstitemFMod_xpath="//li[text()='Forum Moderators']"
    lstitemGuest_xpath="//li[text()='Guests']"
    lstitemReg_xpath="//li[text()='Registered']"
    lstitemVen_xpath="//li[text()='Vendors']"
    drpMVendors_xpath="//select[@id='VendorId']"
    chekbox2_xpath="//input[@id='Active']"
    txtAdmCom_xpath="//textarea[@id='AdminComment']"
    btnSave_xpath="//button[@name='save']"

    #Implement action methods for each locators:
    def __init__(self,driver): #gets the driver from the actual test case and...
        self.driver=driver   #inititates the local driver
    def clickCustomersMenu(self):
        self.driver.find_element(By.XPATH,self.lnk_cust_menu_xpath).click()
    def clickCustomeritemMenu(self):
        self.driver.find_element(By.XPATH,self.lnk_cust_menuitem_xpath).click()
    def clickAddNew(self):
        self.driver.find_element(By.XPATH,self.btnAddnew_xpath).click()
    def enterEmail(self,email):
        self.driver.find_element(By.XPATH,self.txtEmail_xpath).send_keys(email)
    def enterPasswd(self,password):
        self.driver.find_element(By.XPATH,self.txtPass_xpath).send_keys(password)
    def enterFname(self,firstname):
        self.driver.find_element(By.XPATH,self.txtFname_xpath).send_keys(firstname)
    def enterLname(self,lastname):
        self.driver.find_element(By.XPATH,self.txtLname_xpath).send_keys(lastname)
    def setCustomerRoles(self,role):
        self.driver.find_element(By.XPATH, '//*[@id="SelectedCustomerRoleIds_taglist"]/li/span[2]').click()
        self.driver.find_element(By.XPATH,self.lstCustRoles_xpath).click()
        time.sleep(5)
        if role=="Registered":
            self.lstitem=self.driver.find_element(By.XPATH,self.lstitemReg_xpath)
        elif role=="Administrators":
            self.lstitem=self.driver.find_element(By.XPATH,self.lstitemAdm_xpath)
        elif role=="Forum Moderators":
            self.lstitem = self.driver.find_element(By.XPATH,self.lstitemFMod_xpath)
        elif role=="Guests":
            #Here customer can be Registered or Guest, but not two of them same time

            self.lstitem=self.driver.find_element(By.XPATH,self.lstitemGuest_xpath)
        elif role=="Vendors":
            self.lstitem=self.driver.find_element(By.XPATH,self.lstitemVen_xpath)
        else:
            self.lstitem=self.driver.find_element(By.XPATH,self.lstitemGuest_xpath)  #default value
        time.sleep(5)
        self.driver.execute_script("arguments[0].click();",self.lstitem)
    def selectMVendors(self,value):
        drp=Select(self.driver.find_element(By.XPATH,self.drpMVendors_xpath))
        drp.select_by_visible_text(value)
    def selectGender(self,gender):
        if gender=="Male":
            self.driver.find_element(By.XPATH,self.rdmale_xpath).click()
        elif gender=="Female":
            self.driver.find_element(By.XPATH,self.rdFmale_xpath).click()
        else:
            self.driver.find_element(By.XPATH,self.rdmale_xpath).click()  #default value
    def enterDOB(self,DOB):
        self.driver.find_element(By.XPATH,self.txtDOB_xpath).send_keys(DOB)
    def enterCompname(self,company):
        self.driver.find_element(By.XPATH,self.txtComName_xpath).send_keys(company)
    def selectChekbox1(self):
        self.driver.find_element(By.XPATH,self.chekbox1_xpath).click()
    def selectChekbox2(self):
        self.driver.find_element(By.XPATH,self.chekbox2_xpath).click()
    def enterComment(self,comment):
        self.driver.find_element(By.XPATH,self.txtAdmCom_xpath).send_keys(comment)
    def clickSave(self):
        self.driver.find_element(By.XPATH,self.btnSave_xpath).click()
    def clickNewsL(self):
        self.driver.find_element(By.XPATH,self.txtNews_xpath).click()
    def selectStore(self,store):
        if store=="Your store name":
            self.driver.find_element(By.XPATH,self.lstStorname_xpath).click()
        elif store=="Test store 2":
            self.driver.find_element(By.XPATH,self.lstTestStore_xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.lstTestStore_xpath).click()  #default




