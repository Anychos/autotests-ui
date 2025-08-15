from playwright.sync_api import Locator, expect
from elements.base_element import BaseElement
import allure


class TextArea(BaseElement):
    @property
    def type_of(self) -> str:
        return 'text area'

    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        return super().get_locator(nth, **kwargs).locator('textarea').first

    def fill(self, value: str, nth: int = 0, **kwargs):
        with allure.step(f'Заполнение поля "{self.type_of} {self.name}" значением "{value}"'):
            locator = self.get_locator(nth, **kwargs)
            locator.fill(value)

    def check_value(self, value: str, nth: int = 0, **kwargs):
        with allure.step(f'Проверка что значение поля "{self.type_of} {self.name}" соответствует ожидаемому "{value}"'):
            locator = self.get_locator(nth, **kwargs)
            expect(locator).to_have_value(value)

    def clear(self, nth: int = 0, **kwargs):
        with allure.step(f'Очистка поля "{self.type_of} {self.name}"'):
            locator = self.get_locator(nth, **kwargs)
            locator.clear()