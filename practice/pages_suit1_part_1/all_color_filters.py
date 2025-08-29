from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

url = 'https://parsinger.ru/selenium/5.5/5/1.html'

class AllColorSelects:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(url)

    def take_all_color_filters(self):
        HEXes = self.driver.find_elements(By.TAG_NAME, 'span')
        selects = self.driver.find_elements(By.TAG_NAME, 'select')
        checkboxes = self.driver.find_elements(By.CSS_SELECTOR, 'input[type="checkbox"]')
        inputs = self.driver.find_elements(By.CSS_SELECTOR, 'input[type="text"]')
        button_check_result = self.driver.find_elements(By.XPATH, '//button[text()="Проверить"]')

        for HEX in HEXes:
            joint_index = HEXes.index(HEX)
            joint_HEX = HEX.text
            joint_select = selects[joint_index]
            color_blocks = self.driver.find_elements(By.CSS_SELECTOR, 'button[data-hex="' + joint_HEX + '"]')
            joint_color_block = color_blocks[joint_index]
            joint_checkbox = checkboxes[joint_index]
            joint_input = inputs[joint_index]
            joint_button = button_check_result[joint_index]

            Select(joint_select).select_by_value(joint_HEX)
            joint_color_block.click()
            joint_checkbox.click()
            joint_input.send_keys(joint_HEX)
            joint_button.click()

    def click_button_to_check_all_color_filters(self):
        self.driver.find_element(By.XPATH, '//button[text()="Проверить все элементы"]').click()

    def check_result_and_get_key(self):
        key = self.driver.switch_to.alert.text
        print(f'\nYour key:\n{key}')
        assert key.isdigit(), 'Must be alert with big number, it is your key'