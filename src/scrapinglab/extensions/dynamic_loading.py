from .core import BaseExtension
from playwright.async_api import (
    Page,
    Locator,
)

class DynamicLoading(BaseExtension):
    url = 'https://the-internet.herokuapp.com/dynamic_loading'

    async def run(self, page: Page) -> None:
        await page.goto(self.url)
        await self._example_1(page=page)
        await self._example_2(page=page)
        
    async def _example_2(self, page: Page) -> None:
        endpoint = '/2'
        self.logger.info('Attempting example 2...')
        await page.goto(self.url + endpoint)
        button: Locator = page.get_by_role('button', name='Start')
        text: Locator = page.get_by_role(
            'heading', name='Hello World!', level=4)
        self.logger.info('Clicking Start button...')
        await button.click()
        self.logger.info('Loading text into view...')
        await text.wait_for(timeout=10000)
        message: str = await text.inner_text()
        self.logger.info(
            f'Hidden text "{message}" loaded successfully')
        
    async def _example_1(self, page: Page) -> None:
        endpoint = '/1'
        self.logger.info('Attempting example 1...')
        await page.goto(self.url + endpoint)
        button: Locator = page.get_by_role('button', name='Start')
        text: Locator = page.get_by_role(
            'heading', name='Hello World!', level=4)
        self.logger.info('Clicking Start button...')
        await button.click()
        self.logger.info('Changing text state from hidden to visible...')
        await text.wait_for(timeout=10000)
        message: str = await text.inner_text()
        self.logger.info(
            f'Hidden text "{message}" state '
            f'changed from hidden into visible successfully!')
