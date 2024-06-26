import allure

from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage

class MainPage(BasePage):

    @allure.step('Открыть страницу')
    def get_url(self, url):
        self.driver.get(url)

    @allure.step('Кликнуть на кнопку принятия кук')
    def click_button_cookie(self):
        return self.click_to_element(MainPageLocators.MAIN_PAGE_COOKIE_BUTTON)

    @allure.step('Проскролить до списка "Вопросы о важном"')
    def scroll(self):
        self.scroll_down(MainPageLocators.MAIN_PAGE_DOWN_QUESTION_LOCATOR)

    @allure.step("Кликнуть на стрелочку")
    def click_to_arrow(self, number):
        method, locator = MainPageLocators.MAIN_PAGE_QUESTION_LOCATORS
        locator = locator.format(number)
        self.click_to_element((method, locator))

    @allure.step("Получить текст ответа")
    def get_text_under_arrow(self, number):
        method, locator = MainPageLocators.MAIN_PAGE_ANSWER_LOCATOR
        locator = locator.format(number)
        return self.get_text_from_element((method, locator))


    @allure.step('"Посмотреть статус"')
    def check_order_button(self):
        return self.find_element_with_wait(OrderPageLocators.ORDER_PAGE_CHECK_ORDER_BUTTON)