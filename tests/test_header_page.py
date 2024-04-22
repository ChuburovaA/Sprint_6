import pytest
import allure
from constans import Urls

from conftest import driver, main_page, header_page

@allure.feature('Проверка что происходит при нажатии на логотип "Яндекс Самокат"')
class TestHeaderPage: