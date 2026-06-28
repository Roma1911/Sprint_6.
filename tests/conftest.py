import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


@pytest.fixture(scope="function")
def driver():
    firefox_options = Options()
    driver = webdriver.Firefox(options=firefox_options)
    driver.maximize_window()
    driver.get("https://qa-scooter.praktikum-services.ru/")
    yield driver
    driver.quit()