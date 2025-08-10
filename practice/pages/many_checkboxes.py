from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait

url = 'https://parsinger.ru/selenium/4/4.html'

class ManyCheckboxes:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(url)

    def click_all_checkboxes(self):
        checkboxes = self.driver.find_elements(By.CLASS_NAME, 'check')
        for checkbox in checkboxes:
            checkbox.click()

    def click_button(self):
        self.driver.find_element(By.CLASS_NAME,'btn').click()

    def check_and_copy_result_key(self):
        wait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, 'result')))

        result_key = self.driver.find_element(By.ID, 'result')
        print('\nКодовое число:\n' + result_key.text)
        assert result_key.is_displayed(), 'Должно появиться число'