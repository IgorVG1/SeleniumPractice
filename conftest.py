import pytest
import selenium
from selenium import webdriver

@pytest.fixture(scope='session')
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(2)
    print('\nBrowser Chrome was opened\nOptions:\n - FullScreen\n - ImplicitlyWait = 2 sec')
    yield driver
    driver.quit()
    print('\nBrowser was closed')