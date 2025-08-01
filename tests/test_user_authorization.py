from playwright.sync_api import expect, Page
import pytest


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.authorization
@pytest.mark.parametrize("email, password", [
        ("user.name@gmail.com", "password"),
        ("user.name@gmail.com", "  "),
        ("  ", "password")])
def test_authorization_bad_login_password(start_chrome: Page, email: str, password: str):
        start_chrome.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login") # переход на сайт

        email_input = start_chrome.get_by_test_id("login-form-email-input").locator("input") # поиск кнопки login по data-testid
        email_input.fill(email) # заполнение поля email
        password_input = start_chrome.get_by_test_id("login-form-password-input").locator("input")  # поиск поля password
        password_input.fill(password)  # заполнение поля password

        login_button = start_chrome.get_by_test_id("login-page-login-button") # поиск кнопки login
        login_button.click()  # нажатие на кнопку

        wrong_login_message = start_chrome.locator("//div[@data-testid='login-page-wrong-email-or-password-alert']") # поиск сообщения об ошибке
        expect(wrong_login_message).to_be_visible() # ожидание появления элемента
        expect(wrong_login_message).to_contain_text("Wrong email or password") # ожидание содержания текста
        print(wrong_login_message.text_content()) # вывод текста сообщения

        start_chrome.wait_for_timeout(3000) # ожидание 3 секунды. Не используется в реальных тестах
