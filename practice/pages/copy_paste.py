from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/selenium/5.5/4/1.html'

class CopyPaste:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(url)

    def copy_paste_all_text_from_gray_inputs_in_blue_inputs(self):
        inputs_gray = self.driver.find_elements(By.CSS_SELECTOR, 'textarea[color="gray"]')
        inputs_blue = self.driver.find_elements(By.CSS_SELECTOR, 'textarea[color="blue"]')
        inputs_button = self.driver.find_elements(By.CSS_SELECTOR, 'div.parent button')

        for input_g in inputs_gray:
            joint_index = inputs_gray.index(input_g)
            joint_text = input_g.text

            input_g.clear()
            inputs_blue[joint_index].send_keys(joint_text)
            inputs_button[joint_index].click()
    def click_button_to_check_result(self):
        self.driver.find_element(By.ID,'checkAll').click()

    def get_and_check_key(self):
        key = self.driver.find_element(By.ID, 'congrats').text
        print(f'\nYour key:\n{key}')
        assert key is not None, 'Must be text with code same format as XXXX-XXXX-XXXX...'