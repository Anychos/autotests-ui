import pytest
from allure_commons.types import Severity
from pages.authentication.login_page import LoginPage
from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
import allure
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.suites import AllureSuite
from tools.allure.parent_suites import AllureParentSuite
from tools.allure.sub_suites import AllureSubSuite
from config import settings
from tools.routes import AppRoute


@pytest.mark.regression
@pytest.mark.authorization
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.story(AllureStory.AUTHORIZATION)
@allure.parent_suite(AllureParentSuite.LMS)
@allure.suite(AllureSuite.AUTHENTICATION)
@allure.sub_suite(AllureSubSuite.AUTHORIZATION)
class TestAuthorization:
    @pytest.mark.parametrize(
        "email, password",
        [
            ("user.name@gmail.com", "password"),
            ("user.name@gmail.com", "  "),
            ("  ", "password")
        ]
    )
    @allure.title('Авторизация с невалидными паролем или email')
    @allure.severity(Severity.NORMAL)
    def test_wrong_email_or_password_authorization(self, login_page: LoginPage, email: str, password: str):
        login_page.visit(AppRoute.LOGIN)
        login_page.login_form.fill_login_form(email=email, password=password)
        login_page.login_form.check_visible(email=email, password=password)
        login_page.click_login_button()
        login_page.check_visible_wrong_email_or_password_alert()

    @allure.title('Регистрация и авторизация с валидными данными')
    @allure.severity(Severity.BLOCKER)
    def test_successful_authorization(
            self,
            login_page: LoginPage,
            dashboard_page: DashboardPage,
            registration_page: RegistrationPage
    ):
        registration_page.visit(AppRoute.REGISTRATION)
        registration_page.registration_form.fill_registration_form(email=settings.test_user.email, username=settings.test_user.username, password=settings.test_user.password)
        registration_page.click_registration_button()

        dashboard_page.toolbar.check_visible()
        dashboard_page.navbar.check_visible(settings.test_user.username)
        dashboard_page.sidebar.check_visible()
        dashboard_page.sidebar.click_logout()

        login_page.login_form.fill_login_form(email=settings.test_user.email, password=settings.test_user.password)
        login_page.click_login_button()

        dashboard_page.toolbar.check_visible()
        dashboard_page.navbar.check_visible(settings.test_user.username)
        dashboard_page.sidebar.check_visible()

    @allure.title('Навигация со страницы авторизации на страницу регистрации')
    @allure.severity(Severity.NORMAL)
    def test_navigate_from_authorization_to_registration(
            self,
            login_page: LoginPage,
            registration_page: RegistrationPage
    ):
        login_page.visit(AppRoute.LOGIN)
        login_page.click_registration_link()

        registration_page.registration_form.check_visible(email="", username="", password="")