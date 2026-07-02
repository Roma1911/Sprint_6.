
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators import OrderScooterLocators


class OrderPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver, "https://qa-scooter.praktikum-services.ru/")

    @allure.step("Прокручиваем до кнопки Заказать")
    def scroll_to_button_middle(self):
        self.scroll_to_element(OrderScooterLocators.BUTTON_MIDDLE)

    @allure.step("Кликаем кнопку Заказать")
    def click_order_button(self):
        self.click(OrderScooterLocators.ORDER_BUTTON)

    @allure.step("Вводим имя")
    def enter_name(self, name):
        self.send_keys(OrderScooterLocators.NAME_INPUT, name)

    @allure.step("Вводим фамилию")
    def enter_family(self, family):
        self.send_keys(OrderScooterLocators.FAMILY_INPUT, family)

    # @allure.step("Выбираем станцию метро")
    # def enter_station(self, station):
    #     station_input = self.wait.until(EC.visibility_of_element_located(OrderScooterLocators.STATION_INPUT))
    #     station_input.click()
    #     station_input.send_keys(station)
    #     self.wait.until(
    #         EC.visibility_of_element_located((By.XPATH, f"//div[@class='select-search__select']//div[text()='{station}']"))).click()
    
    @allure.step("Выбираем станцию метро")
    def enter_station(self, station):
        self.send_keys(OrderScooterLocators.STATION_INPUT, station)
        station_dropdown_locator = (By.XPATH, f"//div[@class='select-search__select']//div[text()='{station}']")
        self.click(station_dropdown_locator)

    @allure.step("Вводим телефон")
    def enter_phone(self, phone):
        self.send_keys(OrderScooterLocators.TELEPHONE_INPUT, phone)

    @allure.step("Кликаем кнопку Далее")
    def click_next_button(self):
        self.click(OrderScooterLocators.NEXT_BUTTON)

    @allure.step("Вводим дату доставки")
    def enter_delivery_date(self, date):
        date_input = self.wait.until(EC.element_to_be_clickable(OrderScooterLocators.DELIVERY_DATE_FIELD))
        date_input.click()
        date_input.send_keys(date)
        self.click_body()

    @allure.step("Выбираем период аренды 1 сутки")
    def select_rental_period_one_day(self):
        self.click(OrderScooterLocators.RENTAL_PERIOD)
        self.click(OrderScooterLocators.RENTAL_PERIOD_ONE_DAY)

    @allure.step("Выбираем чёрный цвет")
    def select_black_color(self):
        self.click(OrderScooterLocators.BLACK_COLOR)

    @allure.step("Кликаем кнопку Заказать внизу")
    def click_order_middle_button(self):
        self.click(OrderScooterLocators.BUTTON_MIDDLE)

    @allure.step("Кликаем кнопку Да")
    def click_yes_button(self):
        self.click(OrderScooterLocators.BUTTON_YES)

    @allure.step("Проверяем видимость сообщения об успехе")
    def is_success_message_visible(self):
        return self.is_visible(OrderScooterLocators.SUCCESS_MESSAGE)

    @allure.step("Кликаем логотип самоката")
    def select_scooter_img(self):
        self.click(OrderScooterLocators.SCOOTER_IMG)

    @allure.step("Кликаем логотип Яндекса")
    def select_yandex_img(self):
        self.click(OrderScooterLocators.YANDEX_IMG)