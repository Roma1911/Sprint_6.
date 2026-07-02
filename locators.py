from selenium.webdriver.common.by import By


class ScooterLocators:
    
    ARROWS = [
        (By.ID, "accordion__heading-0"),
        (By.ID, "accordion__heading-1"),
        (By.ID, "accordion__heading-2"),
        (By.ID, "accordion__heading-3"),
        (By.ID, "accordion__heading-4"),
        (By.ID, "accordion__heading-5"),
        (By.ID, "accordion__heading-6"),
        (By.ID, "accordion__heading-7"),
    ]

    PANELS = [
        (By.ID, "accordion__panel-0"),
        (By.ID, "accordion__panel-1"),
        (By.ID, "accordion__panel-2"),
        (By.ID, "accordion__panel-3"),
        (By.ID, "accordion__panel-4"),
        (By.ID, "accordion__panel-5"),
        (By.ID, "accordion__panel-6"),
        (By.ID, "accordion__panel-7"),
    ]

    EXPECTED_TEXTS = [
        'Сутки — 400 рублей. Оплата курьеру — наличными или картой.',
        'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.',
        'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.',
        'Только начиная с завтрашнего дня. Но скоро станем расторопнее.',
        'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.',
        'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.',
        'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.',
        'Да, обязательно. Всем самокатов! И Москве, и Московской области.',
    ]



class OrderScooterLocators:

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