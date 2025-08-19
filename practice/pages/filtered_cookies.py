url = 'https://parsinger.ru/methods/3/index.html'

class FilteredCookies:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(url)

    def to_filtere_cookies_and_check_key(self):
        cookies = self.driver.get_cookies()
        filtered_cookies = []
        print('\nFiltered cookies:')
        for cookie in cookies:
            name = cookie['name']
            value = cookie['value']

            if '_' in name:
                parts = name.split('_')
                number_cookie = int(parts[-1])

                if number_cookie % 2 == 0:
                    key_part = int(value)
                    filtered_cookies.append(key_part)
                    print(f'Name:{name}\nValue:{value}')

        key_sum = sum(filtered_cookies)
        print(f'\nYour Key:\n{key_sum}')

        assert key_sum is not None, 'Must be sum values of all filtered cookies'
