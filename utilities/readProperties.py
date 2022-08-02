#this will read data from the config ini file and provide same data to the test case
import configparser

config=configparser.RawConfigParser()  #an object "config" of the class "RawConfigParser"
config.read(".\\Configurations\\config.ini")  #this will read data from the config ini file

class ReadConfig():
    @staticmethod  #can be accessed directly from the class without creating an object.
    def getApplicationURL():
        url=config.get('common info','baseURL')
        return url

    @staticmethod  # can be accessed directly from the class without creating an object.
    def getUserName():
        username = config.get('common info', 'username')
        return username

    @staticmethod  # can be accessed directly from the class without creating an object.
    def getPassword():
        password = config.get('common info', 'password')
        return password