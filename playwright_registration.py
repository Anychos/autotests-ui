from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    """
    инициализация браузера
    """
    browser = playwright.chromium.launch(headless=False) # открытие браузера с графическим интерфейсом

    page = browser.new_page() # открытие новой вкладки
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration") # переход на сайт

    email_input = page.get_by_test_id("registration-form-email-input").locator("input") # поиск поля login
    email_input.fill("user.name@gmail.com") # заполнение поля email
    username_input = page.get_by_test_id("registration-form-username-input").locator("input")  # поиск поля username
    username_input.fill("username")  # заполнение поля username
    password_input = page.get_by_test_id("registration-form-password-input").locator("input")  # поиск поля password
    password_input.fill("password")  # заполнение поля password

    registration_button = page.get_by_test_id("registration-page-registration-button") # поиск кнопки registration
    registration_button.click()  # нажатие на кнопку

    dashboard_title = page.get_by_test_id("dashboard-toolbar-title-text") # поиск заголовка на странице
    expect(dashboard_title).to_be_visible() # ожидание элемента
    print(dashboard_title.text_content()) # вывод текста элемента

    page.wait_for_timeout(3000) # ожидание 3 секунды. Не используется в реальных тестах
