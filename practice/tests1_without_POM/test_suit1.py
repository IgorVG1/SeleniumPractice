import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variables :
url_homepage = 'https://4lapy.ru'

# Проверка функции поиска валидным запросом

def test_1_1(driver):
    valid_search_input = 'cat sterilised'
    driver.get(url_homepage)
    driver.find_element(By.CSS_SELECTOR,'input[placeholder="поиск по товарам"]').send_keys(valid_search_input)

    results = driver.find_elements(By.CSS_SELECTOR,'#id_product_list_root article')
    assert results is not None, 'Должен быть список подходящих товаров'

# Проверка функции поиска невалидным запросом

def test_1_2(driver):
    invalid_search_input = 'panasonic'
    driver.get(url_homepage)
    driver.find_element(By.CSS_SELECTOR,'input[placeholder="поиск по товарам"]').send_keys(invalid_search_input)

    result = driver.find_elements(By.XPATH, '//h1[text()="Страница не найдена"]')
    assert result is not None, 'Должен быть текст: Страница не найдена'
