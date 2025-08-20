from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/selenium/5.5/2/1.html'

class ClearSpecificInputs:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(url)

    def clear_available_inputs(self):
        inputs = self.driver.find_elements(By.TAG_NAME, 'input')
        for input in inputs:
            if input.get_attribute('data-enabled') == 'true':
                input.clear()

    def click_button(self):
        self.driver.find_element(By.TAG_NAME, 'button').click()

    def check_key_in_alert_and_get_him(self):
        alert = self.driver.switch_to.alert
        alert_key = alert.text
        print('\nYour key:\n' + alert_key)
        assert alert_key is not None, 'Alert must contain big number, it it key'