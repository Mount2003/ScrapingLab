from .core import BaseExtension
from playwright.async_api import (
    Page,
    Locator,
)

class MultipleWindows(BaseExtension):
    url = 'https://the-internet.herokuapp.com/windows'

    async def run(self, page: Page) -> None:
        await page.goto(self.url)
        async with (
            page.expect_popup() as popup_info
        ):
            link: Locator = page.get_by_role('link', name='Click Here')
            await link.click()
        popup_page: Page = await popup_info.value
        header: Locator = popup_page.get_by_role('heading', level=3)
        await header.wait_for(state='visible')
        if await header.is_visible():
            text: str = await header.inner_text()
            self.logger.info(f'{text} event successfully intercepted.')