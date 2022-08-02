#This is common for every test case

import logging  #this is a predefine package in python

class LogGen:
    @staticmethod
    def loggen():
        # logging.basicConfig(filename=".\\Logs\\automation.log",
        #         format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = logging.getLogger()
        file_handler = logging.FileHandler(filename=".\\Logs\\automation.log", mode='a')
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logger.setLevel(logging.INFO)
        logger.addHandler(file_handler)
        file_handler.setFormatter(formatter)
        return logger  #it will return logger object which will be use to execute the logs in each event
    