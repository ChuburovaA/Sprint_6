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

    @allure.step('Скролл до нужного элемента')
    def scroll_down(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Ввести номер в элемент')
    def set_number_to_locator(self, locator_num, num):
        method, locator = locator_num
        locator = locator.format(num)
        return method, locator

    @allure.step('Выбрать элемент из выпадающего списка')
    def select_element_from_list(self, locator_menu, locator_item):
        self.click_to_element(locator_menu)
        self.scroll_down(locator_item)
        self.click_to_element(locator_item)

    @allure.step('Дождаться элемента на другой странице')
    def wait_element(self, locator, time=10):
        self.driver.switch_to.window(self.driver.window_handles[1])
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))

    @allure.step('Получить текущую урлу')
    def get_current_url(self):
        return self.driver.current_url