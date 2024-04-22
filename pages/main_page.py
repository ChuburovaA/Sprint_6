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

    @allure.step('Кликнуть на вопрос из списка и просмотреть ответ')
    def click_to_question_and_get_answer_text(self, question, answer, num):
        self.click_to_element(self.set_number_to_locator(question, num))
        return self.get_text_from_element(self.set_number_to_locator(answer, num))