from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path="D:\drivers\ChromeDriver\chromedriver.exe")
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path="D:\drivers\geckoDriver\geckodriver.exe")
    else:
        driver = webdriver.Chrome(executable_path="D:\drivers\ChromeDriver\chromedriver.exe")
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")
###############HTML hookes###############3333


def pytest_configure(config):
    config._metadata['Project Name'] = 'nop commerce'
    config._metadata['Module Name'] = 'nop commerce'
    config._metadata['Tester'] = 'dharitree'

