import time
from re import search

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variables :
base_url = "https://4lapy.ru"

@pytest.fixture()
def driver():
    print("\nBrowser Chrome was opened")
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    print("\nBrowser was closed")
    driver.quit()

class TestMainPage():
    @pytest.mark.skip
    def test_1(self, driver):
        # Open main page and scroll in bottom to link vk group
        driver.get(base_url)
        button_vk_group = driver.find_element(By.XPATH,'(//a[@class="FooterSocial_button__Adt28"])[2]')
        driver.execute_script("return arguments[0].scrollIntoView(true);", button_vk_group)
        button_vk_group.click()

        # Switch to new window with vk group
        vk_group_page = driver.window_handles[1]
        driver.switch_to.window(vk_group_page)

        # Make assert our vk group
        text = driver.find_element(By.CSS_SELECTOR,'div.page_top h1.page_name').text

        assert text == "Зоомагазин Четыре Лапы"

    @pytest.mark.skip
    def test_2(self, driver):
        # Open main page, scroll to button: "Как купить" and click it
        driver.get(base_url)
        button_how_to_buy = driver.find_element(By.XPATH,'(//a[@class="FooterMenu_menuLink__Rwsqp text-b2"])[13]')
        driver.execute_script("return arguments[0].scrollIntoView(true);",button_how_to_buy)
        button_how_to_buy.click()

        # Click button to catalog
        button_to_catalog = driver.find_element(By.XPATH,'//span[text()="В каталог"]')
        button_to_catalog.click()

        input_search = driver.find_element(By.CSS_SELECTOR,'input[placeholder="поиск по товарам"]')
        input_search.send_keys('sterilised cat')

        # Assert search work
        search_results = driver.find_elements(By.TAG_NAME,'article')
        assert search_results is not None

    def test_3(self,driver):
        driver.get(base_url)
        driver.find_element(By.CSS_SELECTOR,'button.HeaderTogglePetServicesBtn_catalogButton__7pZ3l.text-no-wrap').click()
        driver.find_element(By.XPATH, '//div[text()="Онлайн-ветеринария"]').click()

        online_vet_page = driver.window_handles[1]
        driver.switch_to.window(online_vet_page)

        actual_url = driver.current_url
        print(f"Actual url: {actual_url}")
        expected_url = "https://vetsy.ru/veterinars/online/"
        assert actual_url == expected_url, f"{actual_url} is not correct, must be : {expected_url}"