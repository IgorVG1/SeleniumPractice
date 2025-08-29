from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
import time

url = 'https://parsinger.ru/infiniti_scroll_1/'

class InfinityScroll:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(url)

    def scroll_to_tail_list_of_checkboxes_sum_all_numbers_of_each_checkbox_and_check_password(self):
        actions = AC(self.driver)
        all_summand = []
        time.sleep(2)

        for i in range(100):
            checkboxes = self.driver.find_elements(By.CSS_SELECTOR, 'input[type="checkbox"]')
            spans = self.driver.find_elements(By.TAG_NAME, 'span')

            wait(self.driver, 5).until(EC.element_to_be_clickable(checkboxes[i]))

            checkboxes[i].click()
            actions.send_keys(Keys.ARROW_DOWN).perform()
            summand = int(spans[i].text)
            all_summand.append(summand)

        pswd = sum(all_summand)
        print(f'\nYour password:\n{pswd}')
        assert pswd == 86049950, '\nCorrect password:\n86049950'