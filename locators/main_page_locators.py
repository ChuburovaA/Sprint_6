from selenium.webdriver.common.by import By

class MainPageLocators:
    # Вопросы
    MAIN_PAGE_QUESTION_LOCATORS = By.ID, 'accordion__heading-{}'
    MAIN_PAGE_DOWN_QUESTION_LOCATOR = By.ID, 'accordion__heading-7'

    # Ответы
    MAIN_PAGE_ANSWER_LOCATOR = By.ID, 'accordion__panel-{}'

    # Принятие кук
    MAIN_PAGE_COOKIE_BUTTON = By.ID, 'rcc-confirm-button'