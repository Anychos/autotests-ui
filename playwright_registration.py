from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    """
    инициализация браузера
    """
    browser = playwright.chromium.launch(headless=False) # открытие браузера с графическим интерфейсом
    context = browser.new_context()

    page = context.new_page() # открытие новой вкладки
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration") # переход на сайт

    email_input = page.get_by_test_id("registration-form-email-input").locator("input") # поиск поля login
    email_input.fill("user.name@gmail.com") # заполнение поля email
    username_input = page.get_by_test_id("registration-form-username-input").locator("input")  # поиск поля username
    username_input.fill("username")  # заполнение поля username
    password_input = page.get_by_test_id("registration-form-password-input").locator("input")  # поиск поля password
    password_input.fill("password")  # заполнение поля password

    registration_button = page.get_by_test_id("registration-page-registration-button") # поиск кнопки registration
    registration_button.click()  # нажатие на кнопку

    context.storage_state(path="storage_state.json") # сохранение состояния браузера

with sync_playwright() as playwright:
    """
    инициализация браузера с указанием состояния
    """
    browser = playwright.chromium.launch(headless=False) # открытие браузера с графическим интерфейсом
    context = browser.new_context(storage_state="C:\\Users\\anton\\PycharmProjects\\autotests-ui\\storage_state.json")
    page = context.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration") # переход на сайт