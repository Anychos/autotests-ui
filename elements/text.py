from playwright.sync_api import expect
from elements.base_element import BaseElement


class Text(BaseElement):
    def check_text(self, text: str, nth: int = 0, **kwargs):
        locator = self.get_locator(nth,**kwargs)
        expect(locator).to_have_text(text)