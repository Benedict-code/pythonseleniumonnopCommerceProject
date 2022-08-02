from selenium import webdriver
from selenium.webdriver.common.by import  By


class LoginPage():
    # Identify login locators in one class
    testbox_username_xpath="//input[@id='Email']"
    testbox_password_xpath="//input[@id='Password']"
    button_login_xpath="//button[@type='submit']"
    link_logout_xpath="//a[normalize-space()='Logout']"
    #Implement action methods for each locators
    def __init__(self,driver):
        self.driver=driver
    def setUserName(self,username):
        self.driver.find_element(By.XPATH,self.testbox_username_xpath).clear()
        self.driver.find_element(By.XPATH,self.testbox_username_xpath).send_keys(username)
    def setPassword(self,password):
        self.driver.find_element(By.XPATH, self.testbox_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.testbox_password_xpath).send_keys(password)
    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()
    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.link_logout_xpath).click()