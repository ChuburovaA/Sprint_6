import pytest
import allure
from constans import Urls

from conftest import driver, main_page, header_page

@allure.feature('Проверка что происходит при нажатии на логотип "Яндекс Самокат"')
class TestHeaderPage:

    @allure.story('Нажать на логотип "Самокат", попадая при этом на главную странцу "Яндекс Самокат"')
    def test_logo_scooter(self, main_page, header_page):
        main_page.click_button_cookie()
        header_page.click_logo_scooter()
        assert header_page.get_text()