from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/selenium/5.7/1/index.html'

class UranCollecting:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(url)

    def collect_all_uranium_and_check_key(self):
        urans = self.driver.find_elements(By.CLASS_NAME, 'button-container')
        for uran in urans:
            self.driver.execute_script("return arguments[0].scrollIntoView(true);", uran)
            uran.click()

        key = self.driver.switch_to.alert.text
        print(f'\nYour key:\n{key}')
        assert self.driver.switch_to.alert, 'Must be displayed alert with key'