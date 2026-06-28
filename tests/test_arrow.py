import pytest
import allure
from selenium.webdriver.common.by import By
from pages.arrow_page import ScooterPraktikumServices


class TestDropDownList:

    @allure.step('Проверяем текст стрелки 0')
    def test_check_arrow_zero_text(self, driver):
        page = ScooterPraktikumServices(driver)
        page.click_arrow_zero()
        expected_text = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
        actual_text = page.wait_panel_text((By.ID, 'accordion__panel-0'), expected_text)
        assert actual_text == expected_text, f'Ожидаемый текст: "{expected_text}", получен: "{actual_text}"'

    @allure.step('Проверяем текст стрелки 1')
    def test_check_arrow_one_text(self, driver):
        page = ScooterPraktikumServices(driver)
        page.click_arrow_one()
        expected_text = 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'
        actual_text = page.wait_panel_text((By.ID, 'accordion__panel-1'), expected_text)
        assert actual_text == expected_text, f'Ожидаемый текст: "{expected_text}", получен: "{actual_text}"'

    @allure.step('Проверяем текст стрелки 2')
    def test_check_arrow_two_text(self, driver):
        page = ScooterPraktikumServices(driver)
        page.click_arrow_two()
        expected_text = 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'
        actual_text = page.wait_panel_text((By.ID, 'accordion__panel-2'), expected_text)
        assert actual_text == expected_text, f'Ожидаемый текст: "{expected_text}", получен: "{actual_text}"'

    @allure.step('Проверяем текст стрелки 3')
    def test_check_arrow_three_text(self, driver):
        page = ScooterPraktikumServices(driver)
        page.click_arrow_three()
        expected_text = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
        actual_text = page.wait_panel_text((By.ID, 'accordion__panel-3'), expected_text)
        assert actual_text == expected_text, f'Ожидаемый текст: "{expected_text}", получен: "{actual_text}"'

    @allure.step('Проверяем текст стрелки 4')
    def test_check_arrow_four_text(self, driver):
        page = ScooterPraktikumServices(driver)
        page.click_arrow_four()
        expected_text = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'
        actual_text = page.wait_panel_text((By.ID, 'accordion__panel-4'), expected_text)
        assert actual_text == expected_text, f'Ожидаемый текст: "{expected_text}", получен: "{actual_text}"'

    @allure.step('Проверяем текст стрелки 5')
    def test_check_arrow_five_text(self, driver):
        page = ScooterPraktikumServices(driver)
        page.click_arrow_five()
        expected_text = 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'
        actual_text = page.wait_panel_text((By.ID, 'accordion__panel-5'), expected_text)
        assert actual_text == expected_text, f'Ожидаемый текст: "{expected_text}", получен: "{actual_text}"'

    @allure.step('Проверяем текст стрелки 6')
    def test_check_arrow_six_text(self, driver):
        page = ScooterPraktikumServices(driver)
        page.click_arrow_six()
        expected_text = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'
        actual_text = page.wait_panel_text((By.ID, 'accordion__panel-6'), expected_text)
        assert actual_text == expected_text, f'Ожидаемый текст: "{expected_text}", получен: "{actual_text}"'

    @allure.step('Проверяем текст стрелки 7')
    def test_check_arrow_seven_text(self, driver):
        page = ScooterPraktikumServices(driver)
        page.click_arrow_seven()
        expected_text = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
        actual_text = page.wait_panel_text((By.ID, 'accordion__panel-7'), expected_text)
        assert actual_text == expected_text, f'Ожидаемый текст: "{expected_text}", получен: "{actual_text}"'