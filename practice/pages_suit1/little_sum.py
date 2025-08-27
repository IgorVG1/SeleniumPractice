from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/selenium/3/3.html'

class LittleSum:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(url)

    def get_sum_all_numerics_from_each_second_graph_in_table_and_check(self):
        numerics = self.driver.find_elements(By.CSS_SELECTOR, 'div.text p:nth-child(2)')
        sum = 0

        for numeric in numerics:
            sum = sum + int(numeric.text)

        print('\nSum of all numerics on second graph in each table:\n' + str(sum))

        assert sum == 149494128600, 'Сумма должна ровняться числу 149 494 128 600'