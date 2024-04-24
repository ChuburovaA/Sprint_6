import pytest
import allure
from constans import Urls

from conftest import driver, main_page, header_page

@allure.feature('Проверка что происходит при нажатии на логотип "Яндекс Самокат"')
class TestHeaderPage:

    @allure.title('Нажать на логотип "Самокат", попадая при этом на главную странцу "Яндекс Самокат"')
    def test_logo_scooter(self, main_page, header_page):
        main_page.click_button_cookie()
        header_page.click_logo_scooter()
        assert header_page.get_text()

    @allure.title('Нажать на логотип "Яндекса" и в новом окне откроется главная страница "Яндекс Дзена"')
    def test_logo_yandex(self, header_page, main_page):
        main_page.click_button_cookie()
        header_page.click_yandex_logo()
        header_page.switch_to_dzen()
        assert Urls.DZEN_URL in header_page.get_current_url()