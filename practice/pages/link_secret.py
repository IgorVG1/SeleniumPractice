from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/selenium/2/2.html'

class LinkSecret:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(url)

    def find_and_open_secret_link(self):
        self.driver.find_element(By.XPATH,'//a[text()="16243162441624"]').click()

    def check_extra_key(self):
        key = self.driver.find_element(By.ID, 'result')
        assert key.is_displayed(), 'Должно быть поздравление с большим числом'
        print('\nSecret key:\n' + key.text)