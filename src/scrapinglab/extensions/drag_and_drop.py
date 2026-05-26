import asyncio
from playwright.async_api import (
    Page,
    Locator,
)
from .core.base_extension import BaseExtension

class DragAndDrop():
    url = 'https://the-internet.herokuapp.com/drag_and_drop'    

