from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains as AC

url = 'https://parsinger.ru/selenium/7/7.3.4/index.html'

class ContextClick:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(url)

    def context_click_on_target(self):
        actions = AC(self.driver)
        element = self.driver.find_element(By.ID, 'context-area')
        actions.context_click(element).perform()

    def click_to_get_key(self):
        self.driver.find_element(By.CSS_SELECTOR ,'div[data-action="get_password"]').click()

    def get_and_check_key(self):
        key = self.driver.find_element(By.CSS_SELECTOR, 'span[key="access_code"]').text
        print(f'\nYour password:\n{key}')
        assert key is not None, 'In screen must present password'