from playwright.sync_api import Page
import pytest
from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage


@pytest.mark.regression
@pytest.mark.registration
@pytest.mark.smoke
def test_user_registration_positive(start_chrome: Page):
    """
    Тест успешной регистрации пользователя
    """
    registration_page = RegistrationPage(start_chrome)
    registration_page.open_url("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    registration_page.fill_registration_form("s7w8w@example.com", "username", "password")
    registration_page.click_registration_button()
    dashboard_page = DashboardPage(start_chrome)
    dashboard_page.check_visible_dashboard_title()
