from playwright.sync_api import Page, expect
from components.base_component import BaseComponent
from elements.text import Text
import allure


class NavbarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.app_title = Text(page, 'navigation-navbar-app-title-text', 'Navbar app title')
        self.welcome_title = Text(page, 'navigation-navbar-welcome-title-text', 'Navbar welcome title')

    @allure.step('Проверка видимости навбара')
    def check_visible(self, username: str):
        self.app_title.check_visible()
        self.app_title.check_text('UI Course')

        self.welcome_title.check_visible()
        self.welcome_title.check_text(f'Welcome, {username}!')