from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait

url = 'https://parsinger.ru/selenium/5.7/4/index.html'

class InfinityCheckboxes:
    def __init__(self,driver):
        self.driver = driver

    def open(self):
        self.driver.get(url)

    def select_all_odd_checkboxes_in_each_table(self):
        wait(self.driver, 5).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'child_container')))

        target = self.driver.find_element(By.XPATH, '//div[@id="main_container"]')
        actions = AC(self.driver)

        for i in range(20):
            actions.click(target) \
                .send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(
                Keys.ARROW_DOWN) \
                .send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(
                Keys.ARROW_DOWN) \
                .send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(
                Keys.ARROW_DOWN) \
                .perform()

        tables = self.driver.find_elements(By.CLASS_NAME, 'child_container')
        for table in tables:
            checkboxes = table.find_elements(By.TAG_NAME, 'input')
            for checkbox in checkboxes:
                checkbox_value = int(checkbox.get_attribute('value'))
                if checkbox_value % 2 == 0:
                    checkbox.click()

    def click_button_and_check_key_from_alert(self):
        self.driver.find_element(By.CLASS_NAME, 'alert_button').click()

        alert = self.driver.switch_to.alert
        key = alert.text
        print(f'\nYour key:\n{key}')
        assert alert, 'Alert must be displayed with your key'