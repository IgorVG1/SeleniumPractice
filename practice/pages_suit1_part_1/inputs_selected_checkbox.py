from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/selenium/5.5/3/1.html'

class InputsSelectedCheckbox:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(url)

    def check_sum_from_all_inputs_with_selected_checkbox(self):
        checkboxes = self.driver.find_elements(By.TAG_NAME, 'input')
        inputs = self.driver.find_elements(By.TAG_NAME, 'textarea')
        sum = 0

        for checkbox in checkboxes:
            index_checkbox = checkboxes.index(checkbox)
            if checkbox.is_selected():
                summand = int(inputs[index_checkbox].get_attribute('value'))
                sum += summand

        print(f'\nSum of all inputs with selected checkbox:\n{sum}')
        assert sum.is_integer(), 'Must be big number, it is your key'