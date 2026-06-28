import pytest
import allure
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.order_page import QAScooterPraktikumServices


class TestOrderForm:
    test_data = [
        {
            "name": "Иван",
            "family": "Иванов",
            "station": "Бульвар Рокоссовского",
            "phone": "89990001122",
            "date": "02.06.2026",
        },
    ]
    @allure.title("Создать заказ и проверить всплывающее сообщение")

    @pytest.mark.parametrize("order_data", test_data)
    def test_create_order(self, driver, order_data):
        page = QAScooterPraktikumServices(driver)

        page.click_order_button()
        page.enter_name(order_data["name"])
        page.enter_family(order_data["family"])
        page.enter_station(order_data["station"])
        page.enter_phone(order_data["phone"])
        page.click_next_button()
        page.enter_delivery_date(order_data["date"])
        page.select_rental_period_one_day()
        page.select_black_color()
        page.click_order_middle_button()
        page.click_yes_button()
        assert page.is_success_message_visible()

    @allure.title("Логотип Самоката ведет на главную страницу")
    def test_logo_scooter_goes_home(self, driver):
        page = QAScooterPraktikumServices(driver)
        page.select_scooter_img()
        assert driver.current_url == "https://qa-scooter.praktikum-services.ru/"

    @allure.title("Логотип Яндекса открывает Дзен в новом окне")
    def test_logo_yandex_opens_zen(self, driver):
        page = QAScooterPraktikumServices(driver)
        old_windows = driver.window_handles
        page.select_yandex_img()
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(len(old_windows) + 1))
        new_window = [w for w in driver.window_handles if w not in old_windows][0]
        driver.switch_to.window(new_window)
        WebDriverWait(driver, 10).until(lambda d: d.current_url != "about:blank")
        assert "zen" in driver.current_url.lower() or "zen" in driver.title.lower()