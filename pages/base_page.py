import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Найти и убедиться, что элемент виден')
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 7).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Кликнуть на элемент')
    def click_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        element.click()

    @allure.step('Получить текст элемента')
    def get_text_from_element(self, locator):
        element = self.find_element_with_wait(locator)
        return element.text

    @allure.step('Добавить данные')
    def add_text_to_element(self, locator, text):
        element = self.find_element_with_wait(locator)
        element.send_keys(text)