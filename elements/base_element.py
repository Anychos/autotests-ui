from playwright.sync_api import Page, Locator, expect
import allure


class BaseElement:
    def __init__(self, page: Page, locator: str, name: str):
        self.page = page
        self.locator = locator
        self.name = name

    @property
    def type_of(self) -> str:
        return "base element"

    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        locator = self.locator.format(**kwargs)
        with allure.step(f'Получение локатора "{locator}" с индексом {nth}'):
            return self.page.get_by_test_id(locator).nth(nth)

    def click(self, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        with allure.step(f'Клик по элементу "{self.type_of} {self.name}"'):
            locator.click()

    def check_visible(self, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        with allure.step(f'Проверка видимости элемента "{self.type_of} {self.name}"'):
            expect(locator).to_be_visible()

    def check_text(self, text: str, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        with allure.step(f'Проверка, что текст элемента "{self.type_of} {self.name}" соответствует ожидаемому тексту "{text}"'):
            expect(locator).to_have_text(text)