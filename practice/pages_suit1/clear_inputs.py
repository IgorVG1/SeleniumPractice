from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/selenium/5.5/1/1.html'


class ClearInputs:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(url)

    def clear_all_inputs(self):
        inputs = self.driver.find_elements(By.TAG_NAME, 'input')
        for input in inputs:
            input.clear()

    def click_button(self):
        self.driver.find_element(By.TAG_NAME, 'button').click()

    def check_alert_and_take_key_from_alert(self):
        alert = self.driver.switch_to.alert
        key_from_alert = alert.text
        print("\nYour Key :\n" + str(key_from_alert))
        assert key_from_alert is not None, "Alert must contain big number, it's key"
