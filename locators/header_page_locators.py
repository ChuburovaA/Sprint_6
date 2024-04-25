from selenium.webdriver.common.by import By

class HeaderPageLocators:
    # Заголовки "ЯндексСамокат"
    HEADER_PAGE_LOGO_SCOOTER = By.CLASS_NAME, 'Header_LogoScooter__3lsAR'
    HEADER_PAGE_LOGO_YANDEX = By.CLASS_NAME, 'Header_LogoYandex__3TSOI'

    # Заголовок "Самокат на пару дней"
    HEADER_PAGE_TEXT = By.CLASS_NAME, 'Home_Header__iJKdX'

    # Кнопка найти на главной странице Яндекса
    HEADER_PAGE_BUTTON_FIND = By.XPATH, '//button[text()="Найти"]'