import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(driver, 15)
    
    @allure.step("Открывает страницу")
    def open(self):
        self.driver.get(self.url)
    
    @allure.step("Находит элемент")
    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))
    
    @allure.step("Находит несколько элементов")
    def find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))
    
    @allure.step("Кликает на элемент")
    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
    
    @allure.step("Вводит текст в поле")
    def send_keys(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
    
    @allure.step("Скроллит к элементу")
    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element
    
    @allure.step("Скроллит к элементу по центру")
    def scroll_to_element_center(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        return element
    
    @allure.step("Получает текст элемента")
    def get_text(self, locator):
        element = self.find_element(locator)
        return element.text
    
    @allure.step("Проверяет видимость элемента")
    def is_visible(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.is_displayed()
    
    @allure.step("Ждёт появления текста в элементе")
    def wait_text_in_element(self, locator, expected_text):
        self.wait.until(EC.text_to_be_present_in_element(locator, expected_text))
    
    @allure.step("Получает текущий URL")
    def get_current_url(self):
        return self.driver.current_url
    
    @allure.step("Получает заголовок страницы")
    def get_page_title(self):
        return self.driver.title

    @allure.step("Получает все открытые окна")
    def get_window_handles(self):
        return self.driver.window_handles
    
    @allure.step("Переключается на окно")
    def switch_to_window(self, window_handle):
        self.driver.switch_to.window(window_handle)
    
    @allure.step("Кликает по body")
    def click_body(self):
        self.click((By.TAG_NAME, "body"))

    @allure.step("Ждёт новое окно")
    def wait_for_new_window(self, old_windows):
        self.wait.until(EC.number_of_windows_to_be(len(old_windows) + 1))
    
    @allure.step("Ждёт, что URL не blank")
    def wait_for_url_not_blank(self):
        self.wait.until(lambda d: d.current_url != "about:blank")