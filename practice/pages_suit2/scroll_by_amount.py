from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains as AC
import time

url = 'https://parsinger.ru/selenium/7/7.4.1/index.html'

class ScrollByAmount:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(url)

    def scroll_to_step_1_and_do_it(self):
        actions = AC(self.driver)
        actions.scroll_by_amount(0, 750).perform()
        time.sleep(3)

    def scroll_to_step_2_and_do_it(self):
        full_text = self.driver.find_element(By.CSS_SELECTOR, 'div.countdown').text
        parts_text = full_text.split(' ')
        key = parts_text[-1]

        actions = AC(self.driver)
        actions.scroll_by_amount(0, 1500).perform()
        input_key = self.driver.find_element(By.CSS_SELECTOR, 'input[type="text"]')
        input_key.send_keys(key)

    def click_button_to_get_password(self):
        self.driver.find_element(By.TAG_NAME, 'button').click()

        password = self.driver.find_element(By.ID, 'final-key').text
        print(f'\n{password}')