from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait

url = 'https://parsinger.ru/selenium/7/7.html'

class SelectSum:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(url)

    def sum_all_value_options_of_select_and_input_result(self):
        sum = 0

        selects = self.driver.find_elements(By.TAG_NAME, 'option')
        for select in selects:
            sum = sum + int(select.text)

        self.driver.find_element(By.ID, 'input_result').send_keys(sum)

    def click_button(self):
        self.driver.find_element(By.ID,'sendbutton').click()

    def check_key_present(self):
        key = self.driver.find_element(By.ID, 'result')
        print('\nYour Key:\n' + key.text)
        wait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, 'result')))
        assert key.is_displayed()