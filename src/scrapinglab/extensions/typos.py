import re
from re import Match
from typing import Any
from .core import BaseExtension
from playwright.async_api import (
    Page,
    Locator,
)

class Typos(BaseExtension):
    url = 'https://the-internet.herokuapp.com/typos'

    async def run(self, page: Page) -> None:
        while True:
            await page.goto(self.url)
            text: str = await self._get_text(page=page)
            pattern = r'(won.t)\.$'
            found: Match|None = re.search(pattern, string=text)
            if not found:
                raise ValueError('Target word not found.')
            curr_word: Any = found.group(1)
            if curr_word != "won't":
                self.logger.info('Typo detected. Repeating process...')
            else:
                self.logger.info('No typo detected. Breaking loop.')
                break

    async def _get_text(self, page: Page) -> str:
        p_list: list[Locator] = await page.locator(
            'div.example').locator('p').all()
        texts: list = []
        for p in p_list:
            texts.append(await p.inner_text())
        text: str = ' '.join(texts)
        return text
