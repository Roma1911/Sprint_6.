from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Базовый класс для всех страниц"""
    
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(driver, 15)

    def open(self):
        """Открывает страницу"""
        self.driver.get(self.url)

    def find_element(self, locator):
        """Находит элемент"""
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_elements(self, locator):
        """Находит несколько элементов"""
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click(self, locator):
        """Кликает на элемент"""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def send_keys(self, locator, text):
        """Вводит текст в поле"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def scroll_to_element(self, locator):
        """Скроллит к элементу"""
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element

    def scroll_to_element_center(self, locator):
        """Скроллит к элементу по центру"""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        return element

    def get_text(self, locator):
        """Получает текст элемента"""
        element = self.find_element(locator)
        return element.text

    def is_visible(self, locator):
        """Проверяет видимость элемента"""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.is_displayed()

    def wait_text_in_element(self, locator, expected_text):
        """Ждёт появления текста в элементе"""
        self.wait.until(EC.text_to_be_present_in_element(locator, expected_text))

    def get_current_url(self):
        """Получает текущий URL"""
        return self.driver.current_url

    def get_window_handles(self):
        """Получает все открытые окна"""
        return self.driver.window_handles

    def switch_to_window(self, window_handle):
        """Переключается на окно"""
        self.driver.switch_to.window(window_handle)

    def click_body(self):
        """Кликает по body"""
        self.click((By.TAG_NAME, "body"))