from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class QAScooterPraktikumServices:
    ORDER_BUTTON = (By.CLASS_NAME, "Button_Button__ra12g")
    NAME_INPUT = (By.CSS_SELECTOR, 'input[placeholder="* Имя"]')
    FAMILY_INPUT = (By.CSS_SELECTOR, 'input[placeholder="* Фамилия"]')
    STATION_INPUT = (By.CSS_SELECTOR, 'input[placeholder="* Станция метро"]')
    STATION_DROPDOWN_ITEM = (By.XPATH, "//div[@class='select-search__select']//div[text()='Бульвар Рокоссовского']")
    TELEPHONE_INPUT = (By.CSS_SELECTOR, 'input[placeholder="* Телефон: на него позвонит курьер"]')
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее' and contains(@class, 'Button_Button__ra12g')]")
    DELIVERY_DATE_FIELD = (By.CSS_SELECTOR, 'input[placeholder="* Когда привезти самокат"]')
    RENTAL_PERIOD = (By.CLASS_NAME, "Dropdown-control")
    RENTAL_PERIOD_ONE_DAY = (By.XPATH, "//div[contains(@class, 'Dropdown-option') and normalize-space()='сутки']")
    COLOR_SECTION = (By.CLASS_NAME, "Order_Checkboxes__3lWSI")
    BLACK_COLOR = (By.ID, 'black')
    BUTTON_MIDDLE = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']")
    BUTTON_YES = (By.XPATH, "//button[normalize-space()='Да']")
    BUTTON_STATUS = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Посмотреть статус']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(text(), 'Заказ оформлен')]")
    SCOOTER_IMG = (By.CSS_SELECTOR, "img[src='/assets/scooter.svg'][alt='Scooter']")
    YANDEX_IMG = (By.CSS_SELECTOR, "img[src='/assets/ya.svg'][alt='Yandex']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    @allure.step("Прокручиваем до кнопки Заказать")
    def scroll_to_button_middle(self):
        element = self.driver.find_element(*self.BUTTON_MIDDLE)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_order_button(self):
        self.driver.find_element(*self.ORDER_BUTTON).click()

    def enter_name(self, name):
        self.driver.find_element(*self.NAME_INPUT).send_keys(name)

    def enter_family(self, family):
        self.driver.find_element(*self.FAMILY_INPUT).send_keys(family)

    def enter_station(self, station):
        station_input = self.wait.until(EC.visibility_of_element_located(self.STATION_INPUT))
        station_input.click()
        station_input.send_keys(station)
        self.wait.until(
        EC.visibility_of_element_located((By.XPATH, f"//div[@class='select-search__select']//div[text()='{station}']"))).click()

    def enter_phone(self, phone):
        self.driver.find_element(*self.TELEPHONE_INPUT).send_keys(phone)

    def click_next_button(self):
        self.driver.find_element(*self.NEXT_BUTTON).click()

    def enter_delivery_date(self, date):
        date_input = self.wait.until(EC.element_to_be_clickable(self.DELIVERY_DATE_FIELD))
        date_input.click()
        date_input.send_keys(date)
        self.driver.find_element(By.TAG_NAME, "body").click()

    def select_rental_period_one_day(self):
        self.wait.until(EC.element_to_be_clickable(self.RENTAL_PERIOD)).click()
        self.wait.until(EC.element_to_be_clickable(self.RENTAL_PERIOD_ONE_DAY)).click()

    def select_black_color(self):
        self.driver.find_element(*self.BLACK_COLOR).click()

    def click_order_middle_button(self):
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_MIDDLE)).click()
   
    def click_yes_button(self):
        yes = (By.XPATH, "//button[normalize-space()='Да']")
        self.wait.until(EC.presence_of_element_located(yes))
        self.wait.until(EC.element_to_be_clickable(yes)).click()

    def select_button_status(self):
        self.driver.find_element(*self.BUTTON_STATUS).click()

    def is_success_message_visible(self):
        return self.wait.until(EC.visibility_of_element_located(self.SUCCESS_MESSAGE)).is_displayed()

    def select_scooter_img(self):
        self.driver.find_element(*self.SCOOTER_IMG).click()

    def select_yandex_img(self):
        self.driver.find_element(*self.YANDEX_IMG).click()