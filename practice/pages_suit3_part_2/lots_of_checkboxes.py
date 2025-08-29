from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/scroll/2/index.html'

class LotsOfCheckboxes:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(url)

    def sum_all_numbers_from_each_checkbox(self):
        all_summand = []
        checkboxes = self.driver.find_elements(By.CSS_SELECTOR, 'input.checkbox_class')
        spans = self.driver.find_elements(By.TAG_NAME, 'span')

        for checkbox in checkboxes:
            joint_index = checkboxes.index(checkbox)

            checkbox.click()

            summand = spans[joint_index].text
            if summand.isdigit():
                all_summand.append(int(summand))

        sum_up = sum(all_summand)
        print(f'\nSum of all numbers in checkboxes:\n{sum_up}')