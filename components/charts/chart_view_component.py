from playwright.sync_api import Page
from components.base_component import BaseComponent
from elements.Image import Image
from elements.text import Text


class ChartViewComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str, chart_type: str):
        super().__init__(page)

        self.title = Text(page, f'{identifier}-widget-title-text', 'Chart title')
        self.chart = Image(page, f'{identifier}-{chart_type}-chart', 'Chart image')

    def check_visible(self, title: str):
        self.title.check_visible()
        self.title.check_text(title)
        self.chart.check_visible()