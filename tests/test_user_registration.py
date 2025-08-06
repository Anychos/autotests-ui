import pytest
from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage


@pytest.mark.regression
@pytest.mark.registration
@pytest.mark.smoke
def test_user_registration_positive(dashboard_page: DashboardPage, registration_page: RegistrationPage):
    """
    Тест успешной регистрации пользователя
    """
    registration_page.open_url("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    registration_page.fill_registration_form("s7w8w@example.com", "username", "password")
    registration_page.click_registration_button()
    dashboard_page.check_visible_dashboard_title()
