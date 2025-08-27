from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait

url = 'https://parsinger.ru/selenium/7/7.2/index.html'

class ScrollSendKeys:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(url)

    def input_all_form_get_and_check_key(self):
        for i in range(100):
            inputs = self.driver.find_elements(By.CLASS_NAME, 'interactive')
            inputs[i].send_keys('abc')
            inputs[i].send_keys(Keys.ENTER)
            inputs[i].send_keys(Keys.ARROW_DOWN)

        wait(self.driver, 5).until(EC.text_to_be_present_in_element((By.ID, 'hidden-password'), 'Пароль: Wasteland-Survivor-2077'))
        pwd = self.driver.find_element(By.ID, 'hidden-password').text
        print(f'\n{pwd}')
        assert pwd is not None