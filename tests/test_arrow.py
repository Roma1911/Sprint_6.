import pytest
import allure
from pages.arrow_page import ArrowPage
from locators import ScooterLocators


class TestDropDownList:

    @allure.title('Проверка текста стрелок в выпадающем списке')
    @pytest.mark.parametrize("arrow_index", range(8))
    def test_check_arrow_text(self, driver, arrow_index):
        self._check_arrow_text_step(driver, arrow_index)

    @allure.step('Проверяем текст стрелки {arrow_index}')
    def _check_arrow_text_step(self, driver, arrow_index):
        page = ArrowPage(driver)
        page.click_arrow(ScooterLocators.ARROWS[arrow_index])
        expected_text = ScooterLocators.EXPECTED_TEXTS[arrow_index]
        actual_text = page.wait_panel_text(ScooterLocators.PANELS[arrow_index], expected_text)
        assert actual_text == expected_text, f'Ожидаемый текст: "{expected_text}", получен: "{actual_text}"'