from playwright.sync_api import sync_playwright, expect


def test_empty_courses_list():
    """
    Тест пустого списка курсов
    """
    with sync_playwright() as playwright:
        """
        Инициализация браузера
        """
        browser = playwright.chromium.launch(headless=False)  # открытие браузера с графическим интерфейсом
        context = browser.new_context()

        page = context.new_page()  # открытие новой вкладки
        page.goto(
            "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")  # переход на сайт

        email_input = page.get_by_test_id("registration-form-email-input").locator("input")  # поиск поля login
        email_input.fill("user.name@gmail.com")  # заполнение поля email
        username_input = page.get_by_test_id("registration-form-username-input").locator("input")  # поиск поля username
        username_input.fill("username")  # заполнение поля username
        password_input = page.get_by_test_id("registration-form-password-input").locator("input")  # поиск поля password
        password_input.fill("password")  # заполнение поля password

        registration_button = page.get_by_test_id("registration-page-registration-button")  # поиск кнопки registration
        registration_button.click()  # нажатие на кнопку

        context.storage_state(path="storage_state.json")  # сохранение состояния браузера

    with sync_playwright() as playwright:
        """
        Инициализация браузера с указанием состояния
        """
        browser = playwright.chromium.launch(headless=False)  # открытие браузера с графическим интерфейсом
        context = browser.new_context(
            storage_state="C:\\Users\\anton\\PycharmProjects\\autotests-ui\\storage_state.json")
        page = context.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")  # переход на сайт

        courses_page_title = page.locator(
            '//h6[@data-testid="courses-list-toolbar-title-text"]')  # поиск заголовка страницы
        expect(courses_page_title).to_have_text("Courses")
        print("Заголовок страницы 'Courses' найден")

        courses_page_no_results = page.locator(
            '//h6[@data-testid="courses-list-empty-view-title-text"]')  # поиск заголовка страницы
        expect(courses_page_no_results).to_have_text("There is no results")
        print("Заголовок пустого блока 'There is no results' найден")