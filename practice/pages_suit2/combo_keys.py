from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains as AC

url = 'https://parsinger.ru/selenium/7/7.3.3/index.html'

class ComboKeys:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(url)

    def take_combo_needed_keys(self):
        actions = AC(self.driver)
        actions \
            .key_down(Keys.CONTROL) \
            .key_down(Keys.ALT) \
            .key_down(Keys.SHIFT) \
            .send_keys('T') \
            .key_up(Keys.CONTROL) \
            .key_up(Keys.ALT) \
            .key_up(Keys.SHIFT) \
            .perform()

    def get_and_check_key(self):
        key = self.driver.find_element(By.CSS_SELECTOR, 'span[key="access_code"]').text
        print(f'\nYour password:\n{key}')
        assert key is not None, 'In screen must present password'