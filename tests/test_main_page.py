import allure
import pytest
from locators.main_page_locators import MainPageLocators
from data import Answers
from constans import Urls

from conftest import driver, main_page

@allure.feature('Сверка вопросов и ответов в списке "Вопросы о важном"')
class TestMainPage: