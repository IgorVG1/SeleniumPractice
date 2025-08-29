from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/methods/5/index.html'

class OldCookie:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(url)

    def find_link_with_the_oldest_cookie_and_get_him_key(self):
        list_expire_cookie = []

        links = self.driver.find_elements(By.CSS_SELECTOR, 'div.urls')
        for link in links:
            link.click()

            cookies_link = self.driver.get_cookies()
            for cookie_link in cookies_link:
                expiry_cookie = int(cookie_link['expiry'])
                list_expire_cookie.append(expiry_cookie)

            self.driver.back()

        print('\nList of expire all cookie each link:')
        print(list_expire_cookie)

        longest_expire_cookie = max(list_expire_cookie)
        print('\nThe most longest expire of cookie:')
        print(longest_expire_cookie)
        index_extra_cookie = list_expire_cookie.index(longest_expire_cookie)

        links[index_extra_cookie].click()
        key = self.driver.find_element(By.ID, 'result').text
        print(f'\nYour Key:\n{key}')