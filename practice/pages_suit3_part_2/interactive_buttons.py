from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait

url = 'https://parsinger.ru/selenium/5.7/5/index.html'

class InteractiveButtons:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(url)

    def click_all_button_and_check_key(self):
        actions = AC(self.driver)

        buttons = self.driver.find_elements(By.CLASS_NAME, 'timer_button')
        for button in buttons:
            while not button.get_attribute('style') == "background-color: green;":
                actions.click_and_hold(button).perform()

        actions.reset_actions()
        wait(self.driver, 5).until(EC.alert_is_present())
        key = self.driver.switch_to.alert.text
        print(f'\nYour key:\n{key}')
        assert self.driver.switch_to.alert, 'Must be displayed alert with key'