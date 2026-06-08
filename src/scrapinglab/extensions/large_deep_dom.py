from .core import BaseExtension
from playwright.async_api import (
    Page,
    Locator,
)

class LargeDeepDOM(BaseExtension):
    url = 'https://the-internet.herokuapp.com/large'

    async def run(self, page: Page):
        await page.goto(self.url)
        sibling_id = 'div.parent.large-12.columns.tier-1.item-1'
        head = page.locator(sibling_id)
        if await head.is_visible():
            text: str = await head.inner_text()
            numbers = text.split()
            self.logger.info(
                f'Amount of numbers from nested sibling groups:'
                f' {len(numbers)}')
        sibling_count = 0
        while True:
            head = page.locator(sibling_id)
            if await head.is_visible():
                sibling_count += 1
                sibling_id = (
                    f'div.parent.large-12.columns.tier-{
                    sibling_count + 1}.item-1'
                )
            else:
                self.logger.info(f'Total sibling groups: {sibling_count}')
                break
        tbody: Locator = page.locator('tbody')
        tr_list: list[Locator] = await tbody.locator('tr').all()
        amount_num = 0
        for tr in tr_list:
            column_num_list: list[str] = (await tr.inner_text()).split()
            amount_num += len(column_num_list)
        self.logger.info(f'Amount of numbers in table body: {amount_num}')