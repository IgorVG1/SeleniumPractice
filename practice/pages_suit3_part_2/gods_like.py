import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait

url = 'https://parsinger.ru/selenium/7/7.5/index.html'

class GodsLike:
    def __init__(self,driver):
        self.driver = driver

    def open(self):
        self.driver.get(url)

    def likes_all_cards_and_sum_their_values(self):
        actions = AC(self.driver)
        all_summand = []
        wait(self.driver, 5).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'card')))

        for i in range(100):
            cards = self.driver.find_elements(By.CLASS_NAME, 'card')
            cards[i].find_element(By.CLASS_NAME, 'like-btn').click()
            actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).perform()
            time.sleep(0.05)
            summand = int(cards[i].find_element(By.CLASS_NAME, 'big-number').text)
            all_summand.append(summand)

        key = sum(all_summand)
        print(f'\nYour key:\n{key}')