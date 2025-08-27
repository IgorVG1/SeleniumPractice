from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait

url = 'https://parsinger.ru/selenium/7/7.3.5/index.html'

class ScrollToEnd:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(url)

    def scroll_to_end_left_and_right_container(self):
        actions = AC(self.driver)
        lc = self.driver.find_element(By.ID, 'scrollable-container-left')
        rc = self.driver.find_element(By.ID, 'scrollable-container-right')
        actions \
            .click(lc).send_keys(Keys.END) \
            .click(rc).send_keys(Keys.END) \
            .perform()

    def get_and_check_key(self):
        wait(self.driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[key="access_code"]')))
        key = self.driver.find_element(By.CSS_SELECTOR, 'span[key="access_code"]').text
        print(f'\nYour password:\n{key}')
        assert key is not None, 'In screen must present password'