Запуск тестов:
    # Запустить все тесты из файла
    pytest tests/test_arrow.py -v
    pytest tests/test_order_and_scroll.py -v
    pytest tests/test_logo.py -v

    # Запустить тесты с отчётом Allure
    pytest tests/test_arrow.py --alluredir=./allure-results
    allure serve ./allure-results

    pytest tests/test_order_and_scroll.py --alluredir=./allure-results
    allure serve ./allure-results

    pytest tests/test_logo.py --alluredir=./allure-results
    allure serve ./allure-results
    
    # Запустить конкретный тест
    pytest tests/test_arrow.py::TestDropDownList::test_check_arrow_text[0] -v

    pytest tests/test_order_and_scroll.py::TestOrder::test_create_order_via_top_button -v

    pytest tests/test_logo.py::TestLogo::test_logo_scooter_goes_home -v

