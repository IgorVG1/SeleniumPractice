from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains as AC

url = 'https://parsinger.ru/infiniti_scroll_3/'

class ManyScrollContainers:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(url)

    def scroll_to_tail_all_containers_and_sum_all_numbers_of_each(self):
        actions = AC(self.driver)
        scroll_containers = self.driver.find_elements(By.XPATH, '//div[@class="main"]/div')
        all_sum_of_container = []

        for container in scroll_containers:

            target = container.find_element(By.CSS_SELECTOR, 'div div')
            all_summand = []

            for i in range(8):
                actions.click(target) \
                    .send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN) \
                    .send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN) \
                    .send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).perform()

            spans = container.find_elements(By.TAG_NAME, 'span')

            for span in spans:
                summand = int(span.text)
                all_summand.append(summand)

            sum_of_container = sum(all_summand)
            print(f'\nSum of container #{scroll_containers.index(container)}:\n{sum_of_container}')
            all_sum_of_container.append(sum_of_container)

        pswd = sum(all_sum_of_container)
        print(f'\nYour password:\n{pswd}')