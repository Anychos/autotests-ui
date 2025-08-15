from playwright.sync_api import expect
from elements.base_element import BaseElement
import allure


class Text(BaseElement):
    @property
    def type_of(self) -> str:
        return 'text'

    def check_text(self, text: str, nth: int = 0, **kwargs):
        with allure.step(f'Проверка что текст в элементе"{self.type_of} {self.name}" соответствует ожидаемому "{text}"'):
            locator = self.get_locator(nth,**kwargs)
            expect(locator).to_have_text(text)