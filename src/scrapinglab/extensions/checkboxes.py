import logging
import asyncio
from logging import Logger
from playwright.async_api import (
    Page,
    Browser,
    Locator,
    BrowserContext
)

class CheckBoxes:
    def __init__(self, browser: Browser|None = None) -> None:
        self.browser: Browser = browser
        self.url: str = 'https://the-internet.herokuapp.com/checkboxes'        
        self.logger: Logger = logging.getLogger(self.__class__.__name__)
    
    async def init_extension(self) -> None:
        page: Page
        context: BrowserContext
        async with (
            await self.browser.new_context() as context,
            await context.new_page() as page,
        ):
            await page.goto(self.url)
            if await self._click_checkbox(page=page):
                self.logger.info('Checkbox stage done...')

    async def _click_checkbox(self, page: Page|None = None) -> bool:
        checkbox_list: list[Locator] = await page.get_by_role(
            'checkbox').all()
        for id, checkbox in enumerate(checkbox_list, start=1):
            status_ticked: bool = await checkbox.is_checked()
            if status_ticked:
                self.logger.info(f'Checkbox{id} is checked, '
                    'proceed to uncheck it...')
                await checkbox.set_checked(not status_ticked)
            else:
                self.logger.info(f'Checkbox{id} is unchecked, '
                    'proceed to check it...')
                await checkbox.set_checked(not status_ticked)
            await asyncio.sleep(1.5)
        return True

