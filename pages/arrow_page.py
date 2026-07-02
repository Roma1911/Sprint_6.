
import allure
from pages.base_page import BasePage
from locators import ScooterLocators


class ArrowPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver, "https://qa-scooter.praktikum-services.ru/")

    @allure.step('Прокручиваем до подзаголовка')
    def scroll_to_subheader(self):
        self.scroll_to_element_center(ScooterLocators.ARROWS[0])

    @allure.step('Кликаем на стрелку')
    def click_arrow(self, locator):
        self.scroll_to_element_center(locator)
        self.click(locator)

    @allure.step('Ждём текст в панели и получаем его')
    def wait_panel_text(self, panel_locator, expected_text):
        self.wait_text_in_element(panel_locator, expected_text)
        return self.get_text(panel_locator)