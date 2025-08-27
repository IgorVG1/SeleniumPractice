from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/scroll/4/index.html'

class ClosedNumbers:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(url)

    def click_all_buttons_check_and_get_key(self):
        buttons = self.driver.find_elements(By.TAG_NAME, 'button')
        sum = 0

        for button in buttons:
            self.driver.execute_script("return arguments[0].scrollIntoView(true);", button)
            button.click()
            number = int(self.driver.find_element(By.ID, 'result').text)
            sum += number

        print(f'\nYour key:\n{sum}')
        assert sum is not None, "Must be big number. It is your key"