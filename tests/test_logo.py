
import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.order_page import OrderPage
from constants import MAIN_URL


class TestLogo:

    @allure.title("Логотип Самоката ведет на главную страницу")
    def test_logo_scooter_goes_home(self, driver):
        page = OrderPage(driver)
        page.click_order_button()
        page.select_scooter_img()
        assert page.is_on_home_page()

    @allure.title("Логотип Яндекса открывает Дзен в новом окне")
    def test_logo_yandex_opens_zen(self, driver):
        page = OrderPage(driver)
        assert page.is_zen_opened_in_new_window()