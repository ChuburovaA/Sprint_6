import allure
import pytest
from locators.main_page_locators import MainPageLocators
from data import Answers
from constans import Urls

from conftest import driver, main_page

@allure.feature('Сверка вопросов и ответов в списке "Вопросы о важном"')
class TestMainPage:
    @pytest.mark.parametrize(
        "q_num,expected_result",
        [
            (0, Answers.ANSWER_0),
            (1, Answers.ANSWER_1),
            (2, Answers.ANSWER_2),
            (3, Answers.ANSWER_3),
            (4, Answers.ANSWER_4),
            (5, Answers.ANSWER_5),
            (6, Answers.ANSWER_6),
            (7, Answers.ANSWER_7)
        ]
    )
    def test_questions(self, main_page, q_num, expected_result):

        main_page.get_url(Urls.URL)
        main_page.click_button_cookie()
        main_page.scroll()
        result = main_page.click_to_question_and_get_answer_text(
            MainPageLocators.MAIN_PAGE_QUESTION_LOCATORS,
            MainPageLocators.MAIN_PAGE_ANSWER_LOCATOR,
            q_num
        )

        assert main_page.check_answer_correct(result, expected_result)