
from selenium.webdriver.common.by import By

url = 'https://4lapy.ru'

class HomePage():

    def __init__(self,driver):
        self.driver = driver

    def open(self):
        self.driver.get(url)

    def search(self, search_input):
        self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="поиск по товарам"]').send_keys(search_input)

    def check_search_result_with_valid_input(self):
        result = self.driver.find_elements(By.CSS_SELECTOR, '#id_product_list_root article')
        assert result is not None, 'Должен быть список подходящих товаров'

    def check_search_result_with_invalid_input(self):
        result = self.driver.find_elements(By.XPATH, '//h1[text()="Страница не найдена"]')
        assert result is not None, 'Должен быть текст: Страница не найдена'