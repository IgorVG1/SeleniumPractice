from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/methods/3/index.html'

class SecretCookies:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(url)

    def sum_values_from_all_secret_cookies_and_get_key(self):
        cookies = self.driver.get_cookies()
        values_secret_cookies = []

        for cookie in cookies:
            if 'secret_cookie_' in cookie['name']:
                value_cookie = int(cookie['value'])
                values_secret_cookies.append(value_cookie)

        key = sum(values_secret_cookies)
        print(f'\nYour key:\n{key}')