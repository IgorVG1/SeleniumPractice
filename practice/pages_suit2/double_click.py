from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains as AC

url = 'https://parsinger.ru/selenium/7/7.3.2/index.html'

class DoubleClick:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(url)

    def double_click_on_target(self):
        actions = AC(self.driver)
        element = self.driver.find_element(By.ID, 'dblclick-area')
        actions.double_click(element).perform()

    def get_and_check_key(self):
        pwd = self.driver.find_element(By.ID, 'password').text
        print(f'\nYour password:\n{pwd}')
        assert pwd is not None, 'In screen must present password'