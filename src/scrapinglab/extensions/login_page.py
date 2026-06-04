from .core import BaseExtension
from playwright.async_api import (
    Page,
    Locator,
)

class LoginPage(BaseExtension):
    url = 'https://the-internet.herokuapp.com/login'

    async def run(self, page: Page) -> None:
        await page.goto(self.url)
        username = 'random'
        password = 'RANDOM'
        await self._login_with_creds(
            page=page, username=username, password=password)
        username = 'tomsmith'
        password = 'SuperSecretPassword!'
        await self._login_with_creds(
            page=page, username=username, password=password)

    async def _login_with_creds(
        self,
        page: Page, 
        username: str, 
        password: str) -> bool:
        username_input: Locator = page.get_by_role(
            'textbox', name='Username')
        password_input: Locator = page.get_by_role(
            'textbox', name='Password')
        await self._hover_and_focus(textbox=username_input)
        await username_input.press_sequentially(text=username, delay=50)
        await self._hover_and_focus(textbox=password_input)
        await password_input.press_sequentially(text=password, delay=50)
        button: Locator = page.get_by_role("button", name=" Login")
        await button.click()
        status: bool = await self._check_result(page=page)
        return status

    async def _check_result(self, page:Page) -> bool:
        div_result: Locator = page.locator('div#flash')
        result: str|None = await div_result.get_attribute('class')
        if result is not None:
            if 'success' in result:
                self.logger.info('Form authentication successful.')
                return True
            else:
                self.logger.info('Form authentication failed.')
                return False
        else:
            raise ValueError('Failed to get value from result element.')

    async def _hover_and_focus(self, textbox: Locator) -> None:
        await textbox.hover()
        await textbox.focus()
