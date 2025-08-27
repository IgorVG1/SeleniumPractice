from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains as AC

url = 'https://parsinger.ru/selenium/7/7.3.1/index.html'

class DragAndDrop:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(url)

    def drag_and_drop_target(self):
        actions = AC(self.driver)
        source = self.driver.find_element(By.ID, 'draggable')
        target = self.driver.find_element(By.ID, 'target')
        actions.drag_and_drop(source, target).perform()

    def get_and_check_key(self):
        pwd = self.driver.find_element(By.ID, 'password').text
        print(f'\nYour password:\n{pwd}')
        assert pwd is not None, 'In screen must present password'