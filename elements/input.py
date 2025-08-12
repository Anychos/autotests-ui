from playwright.sync_api import expect, Locator

from elements.base_element import BaseElement


class Input(BaseElement):
    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        return super().get_locator(**kwargs).locator('input').nth(nth)

    def fill(self, value: str, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        locator.fill(value)

    def check_value(self, value: str, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        expect(locator).to_have_value(value)

    def clear(self, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        locator.clear()