import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains as AC

url = 'https://parsinger.ru/infiniti_scroll_2/'

class InfinityScroll2:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(url)
        time.sleep(1)

    def scroll_to_tail_and_sum_all_numbers(self):
        actions = AC(self.driver)
        all_summand = []

        for i in range(100):
            tables = self.driver.find_elements(By.TAG_NAME, 'p')
            actions.move_to_element(tables[i]).send_keys(Keys.ARROW_DOWN).perform()

            summand = int(tables[i].text)
            all_summand.append(summand)

        summa = sum(all_summand)
        print(f'\nSum of all numbers:\n{summa}')