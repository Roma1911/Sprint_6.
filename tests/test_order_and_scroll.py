import pytest
import allure
from pages.order_page import OrderPage
from data import ORDER_TEST_DATA


class TestOrder:

    @allure.title("Создать заказ через кнопку Заказать вверху страницы")
    @pytest.mark.parametrize("order_data", [ORDER_TEST_DATA[0]])
    def test_create_order_via_top_button(self, driver, order_data):
        page = OrderPage(driver)
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

    @allure.title("Создать заказ через кнопку Заказать внизу страницы")
    @pytest.mark.parametrize("order_data", [ORDER_TEST_DATA[1]])
    def test_create_order_via_bottom_button(self, driver, order_data):
        page = OrderPage(driver)
        page.scroll_to_button_middle()
        page.click_order_middle_button()
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
