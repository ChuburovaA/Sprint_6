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