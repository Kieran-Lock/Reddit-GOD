from playwright.sync_api import Locator
from .screenshotter import RedditScreenshotter


class RedditComment:
    def __init__(self, screenshotter: RedditScreenshotter, locator: Locator, content: str):
        self.content = content
        self.screenshot = screenshotter.screenshot_comment(locator)
