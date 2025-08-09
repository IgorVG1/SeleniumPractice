from  selenium.webdriver.common.by import By

url = 'https://parsinger.ru/selenium/3/3.html'

class GrandSum:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(url)

    def get_sum_all_numerics_from_all_tables_and_check(self):
        tables = self.driver.find_elements(By.CLASS_NAME, 'text')
        sum = 0

        for table in tables:
            numerics = table.find_elements(By.TAG_NAME, 'p')
            for numeric in numerics:
                sum = sum + int(numeric.text)

        print('\nSum of all numerics:\n' + str(sum))

        assert sum == 450384194300, 'Сумма должна ровняться числу 450 384 194 300'