from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class ScooterPraktikumServices:
    arrow_zero = (By.ID, "accordion__heading-0")
    arrow_one = (By.ID, "accordion__heading-1")
    arrow_two = (By.ID, "accordion__heading-2")
    arrow_three = (By.ID, "accordion__heading-3")
    arrow_four = (By.ID, "accordion__heading-4")
    arrow_five = (By.ID, "accordion__heading-5")
    arrow_six = (By.ID, "accordion__heading-6")
    arrow_seven = (By.ID, "accordion__heading-7")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    @allure.step('Прокручиваем до подзаголовка')
    def scroll_to_subheader(self):
        element = self.wait.until(EC.visibility_of_element_located(self.arrow_zero))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    @allure.step('Кликаем на стрелку')
    def click_arrow(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.wait.until(EC.element_to_be_clickable(locator)).click()
    
    def wait_panel_text(self, panel_locator, expected_text):
        self.wait.until(EC.text_to_be_present_in_element(panel_locator, expected_text))
        return self.driver.find_element(*panel_locator).text

    @allure.step('Кликаем на стрелку 0')
    def click_arrow_zero(self):
        self.click_arrow(self.arrow_zero)

    @allure.step('Кликаем на стрелку 1')
    def click_arrow_one(self):
        self.click_arrow(self.arrow_one)

    @allure.step('Кликаем на стрелку 2')
    def click_arrow_two(self):
        self.click_arrow(self.arrow_two)

    @allure.step('Кликаем на стрелку 3')
    def click_arrow_three(self):
        self.click_arrow(self.arrow_three)

    @allure.step('Кликаем на стрелку 4')
    def click_arrow_four(self):
        self.click_arrow(self.arrow_four)

    @allure.step('Кликаем на стрелку 5')
    def click_arrow_five(self):
        self.click_arrow(self.arrow_five)

    @allure.step('Кликаем на стрелку 6')
    def click_arrow_six(self):
        self.click_arrow(self.arrow_six)

    @allure.step('Кликаем на стрелку 7')
    def click_arrow_seven(self):
        self.click_arrow(self.arrow_seven)