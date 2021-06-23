----------------------- Проверка flake8 пройдена -----------------------

============================= test session starts ==============================
platform linux -- Python 3.7.4, pytest-5.3.2, py-1.10.0, pluggy-0.13.1 -- /usr/local/bin/python
rootdir: /app, inifile: pytest.ini, testpaths: tests/
plugins: django-3.8.0
collecting ... collected 20 items

tests/test_homework.py::TestRecord::test_init[kwargs0] PASSED            [  5%]
tests/test_homework.py::TestRecord::test_init[kwargs1] PASSED            [ 10%]
tests/test_homework.py::TestCalculator::test_init PASSED                 [ 15%]
tests/test_homework.py::TestCalculator::test_add_record PASSED           [ 20%]
tests/test_homework.py::TestCalculator::test_get_today_stats PASSED      [ 25%]
tests/test_homework.py::TestCalculator::test_get_week_stats FAILED       [ 30%]
tests/test_homework.py::TestCalculator::test_get_calories_remained PASSED [ 35%]
tests/test_homework.py::TestCalculator::test_get_today_cash_remained PASSED [ 40%]
tests/test_homework.py::TestCaloriesCalculator::test_init PASSED         [ 45%]
tests/test_homework.py::TestCaloriesCalculator::test_get_calories_remained PASSED [ 50%]
tests/test_homework.py::TestCashCalculator::test_init PASSED             [ 55%]
tests/test_homework.py::TestCashCalculator::test_get_today_cash_remained[0-usd] PASSED [ 60%]
tests/test_homework.py::TestCashCalculator::test_get_today_cash_remained[0-eur] PASSED [ 65%]
tests/test_homework.py::TestCashCalculator::test_get_today_cash_remained[0-rub] PASSED [ 70%]
tests/test_homework.py::TestCashCalculator::test_get_today_cash_remained[1-usd] FAILED [ 75%]
tests/test_homework.py::TestCashCalculator::test_get_today_cash_remained[1-eur] FAILED [ 80%]
tests/test_homework.py::TestCashCalculator::test_get_today_cash_remained[1-rub] PASSED [ 85%]
tests/test_homework.py::TestCashCalculator::test_get_today_cash_remained[-1-usd] FAILED [ 90%]
tests/test_homework.py::TestCashCalculator::test_get_today_cash_remained[-1-eur] FAILED [ 95%]
tests/test_homework.py::TestCashCalculator::test_get_today_cash_remained[-1-rub] PASSED [100%]

=================================== FAILURES ===================================
/app/tests/test_homework.py:100: AssertionError: Необходимо считать сколько денег потрачено за последние 7 дней
/app/tests/test_homework.py:203: AssertionError: Проверьте правильность работы метода `get_today_cash_remained()` у класса `CashCalculator`
/app/tests/test_homework.py:203: AssertionError: Проверьте правильность работы метода `get_today_cash_remained()` у класса `CashCalculator`
/app/tests/test_homework.py:203: AssertionError: Проверьте правильность работы метода `get_today_cash_remained()` у класса `CashCalculator`
/app/tests/test_homework.py:203: AssertionError: Проверьте правильность работы метода `get_today_cash_remained()` у класса `CashCalculator`
========================= 5 failed, 15 passed in 0.19s =========================
