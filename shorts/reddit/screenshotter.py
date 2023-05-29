from __future__ import annotations
from contextlib import contextmanager
from io import BytesIO
from typing import ContextManager
from playwright.sync_api import sync_playwright, Page, Locator


class RedditScreenshotter:
    def __init__(self, page: Page):
        self.page = page

    @staticmethod
    def screenshot_comment(comment_locator: Locator) -> BytesIO:
        return BytesIO(comment_locator.screenshot())

    def screenshot_post(self) -> BytesIO:
        return BytesIO(self.page.locator("shreddit-post").screenshot())


@contextmanager
def reddit_screenshots(url: str) -> ContextManager[RedditScreenshotter]:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)
        screenshotter = RedditScreenshotter(page)
        try:
            yield screenshotter
        finally:
            browser.close()
