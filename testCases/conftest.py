from selenium import webdriver
import pytest


#@pytest.fixture()
# def setup()
#     driver=webdriver.Chrome()
#     return driver

@pytest.fixture()
def setup(browser):
    if browser=="edge":
        driver=webdriver.Edge()
        print("Launching Edge browser...")
    elif browser=="firefox":
        driver=webdriver.Firefox()
        print("Launching Firefox browser...")
    else:
        driver=webdriver.Chrome()
    return driver

def pytest_addoption(parser):  #This will get the value from the CLI/hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  #This will return the Browser value to setup method
    return request.config.getoption("--browser")

########### PYTEST HTML REPORT ##############
#It is hook for adding environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Ben'

#It is hook for delete/modify environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)