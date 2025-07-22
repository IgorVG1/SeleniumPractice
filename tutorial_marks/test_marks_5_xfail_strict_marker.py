from email.policy import strict

import pytest

@pytest.mark.xfail(strict=True)
def test_succeed():
    assert True


@pytest.mark.xfail
def test_not_succeed():
    assert False


@pytest.mark.skip
def test_skipped():
    assert False

# Наш упавший тест теперь отмечен как xfail, но результат прогона тестов помечен как успешный
# Кстати, к маркировке xfail можно добавлять параметр strict (строгий).
# Если функция будет отображаться в выходных данных терминала так, как будто она завершается сбоем,
# но если она неожиданно завершится успешно, то набор тестов завершится неудачно.
# (Если тест, который должен был упасть, неожиданно пройдет, то мы это заметим в отчете - он будет красный)

# >>> pytest -v test_marks_5_xfail_strict_marker.py