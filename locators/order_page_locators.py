from selenium.webdriver.common.by import By

class OrderPageLocators:
    # Страница "Для кого самокат"
    ORDER_PAGE_NAME = By.XPATH, '//input[@placeholder="* Имя"]'
    ORDER_PAGE_SURNAME = By.XPATH, '//input[@placeholder="* Фамилия"]'
    ORDER_PAGE_ADDRESS = By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]'

    ORDER_PAGE_METRO_STATION_BUTTON = By.XPATH, '//div[@class="select-search__value"]'
    ORDER_PAGE_METRO_STATION = By.XPATH, '//div[@class="select-search__select"]/ul/li[@data-index="{}"]'

    ORDER_PAGE_PHONE_NUMBER = By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]'

    ORDER_PAGE_BUTTON_NEXT = By.XPATH, '//button[text()="Далее"]'

    # Страница "Про аренду"
    ORDER_PAGE_DATE = By.XPATH, '//input[@placeholder="* Когда привезти самокат"]'
    ORDER_PAGE_ACCEPT_DATE = By.XPATH, '//div[@class="Order_Header__BZXOb" and text()="Про аренду"]'

    ORDER_PAGE_RENT_TIME = By.XPATH, '//div[@class="Dropdown-root"]'
    ORDER_PAGE_RENT_TO_ONE_DAY = By.XPATH, '//div[@class="Dropdown-option" and text()="сутки"]'
    ORDER_PAGE_RENT_TO_TWO_DAYS = By.XPATH, '//div[@class="Dropdown-option" and text()="двое суток"]'

    ORDER_PAGE_BLACK_CHECKBOX = By.XPATH, '//input[@id="black"]'
    ORDER_PAGE_GREY_CHECKBOX = By.XPATH, '//input[@id="grey"]'

    ORDER_PAGE_COMMENT_FOR_COURIER = By.XPATH, '//input[@placeholder="Комментарий для курьера"]'

    ORDER_PAGE_ORDER_BUTTON = By.XPATH, '//div[@class="Order_Buttons__1xGrp"]/button[text()="Заказать"]'

    # Окно "Хотите оформить заказ?"
    ORDER_PAGE_BUTTON_YES = By.XPATH, '//button[text()="Да"]'

    # Окно подтверждвющие сделанный заказ с переходом на просмотр статуса заказа
    ORDER_PAGE_CHECK_ORDER_BUTTON = By.XPATH, '//button[text()="Посмотреть статус"]'

    # Кнопки "Заказать" находящиеся на главной странице "ЯндексСамокат"
    ORDER_BUTTON_UP = By.XPATH, '//div[@class="Header_Nav__AGCXC"]/button[text()="Заказать"]'
    ORDER_BUTTON_DOWN = By.XPATH, '//div[@class="Home_FinishButton__1_cWm"]/button[text()="Заказать"]'