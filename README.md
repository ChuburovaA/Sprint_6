# Sprint_6
## Написание автотеста для учебного сервиса "Яндекс.Самокат"
### Структура проекта:
1. Все локаторы находятся в папке - locators
2. Отдельный класс РОМ в папке - pages
3. Все тесты находятся в папке - tests
4. Фикстуры распологаются в файле - conftest.py
5. URL распологается в файле - constans.py
6. Класс с вопросами и ответами списка "Вопросы о важном" в файле data.py
7. В файле requirements.txt находятся системные настройки
8. Описание теста распологается в файле - README.md

### Краткое описание тестов:
1. Проверка нажатия на логотип "Яндекс.Самокат" - test_header_page.py
Проверяли что при нажатии на "Самокат" будет переход на главную страницу "Яндекс.Самокат", а при нажатии на "Яндекс" будет происходить переход на страницу "Яндекс.Дзен"
2. Проверка выпадающего списка раздела "Вопросы о важном" - test_main_page.py
Проверяли, что при нажатии на стрелку, будет происходить соответсвующий текст
3. Проверка оформления заказа  - test_order_page.py
Проверяли, что при нажатии вверхней и нижней кнопок "Заказать", заполнении всех полей заказ будет успешно совершен.

