from .core import BaseExtension
from playwright.async_api import (
    Page,
    Locator,
)

class KeyPresses(BaseExtension):
    url = 'https://the-internet.herokuapp.com/key_presses'

    async def run(self, page: Page):
        await page.goto(self.url)
        input: Locator = page.locator("#target")
        text: str = 'Test123'
        await input.focus()
        for i, t in enumerate(text, start=1):
            await input.press(t)
            await self._display_result(page=page)
            if i == len(text):
                await input.press('Enter')
                self.logger.info('You entered: ENTER')

    async def _display_result(self, page: Page):
        result: Locator = page.locator('p#result')
        result_str: str = await result.inner_text()
        self.logger.info(result_str)