from playwright.sync_api import sync_playwright, expect
import pytest


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.authorization
def test_authorization_bad_login_password():
    with sync_playwright() as playwright:
        """
        Инициализация браузера
        """
        browser = playwright.chromium.launch(headless=False) # headless=True - без графического интерфейса

        page = browser.new_page() # открытие новой вкладки
        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login") # переход на сайт

        email_input = page.get_by_test_id("login-form-email-input").locator("input") # поиск кнопки login по data-testid
        email_input.fill("test@mail.ru") # заполнение поля email
        password_input = page.get_by_test_id("login-form-password-input").locator("input")  # поиск поля password
        password_input.fill("qwerty123")  # заполнение поля password

        login_button = page.get_by_test_id("login-page-login-button") # поиск кнопки login
        login_button.click()  # нажатие на кнопку

        wrong_login_message = page.locator("//div[@data-testid='login-page-wrong-email-or-password-alert']") # поиск сообщения об ошибке
        expect(wrong_login_message).to_be_visible() # ожидание появления элемента
        expect(wrong_login_message).to_contain_text("Wrong email or password") # ожидание содержания текста
        print(wrong_login_message.text_content()) # вывод текста сообщения

        page.wait_for_timeout(3000) # ожидание 3 секунды. Не используется в реальных тестах
