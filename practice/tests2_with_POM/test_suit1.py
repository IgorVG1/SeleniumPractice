from practice.pages.homepage import HomePage



# Проверка функции поиска валидным запросом
def test_1_1(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.search('cat sterilised')
    homepage.check_search_result_with_valid_input()

# Проверка функции поиска невалидным запросом
def test_1_2(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.search('panasonic')
    homepage.check_search_result_with_invalid_input()
