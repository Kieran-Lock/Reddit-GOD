import itertools
from typing import Iterator
from .comment import RedditComment
from .screenshotter import reddit_screenshots, RedditScreenshotter


class RedditSubmission:
    def __init__(self, url: str, author: str, title: str, text: str, maximum_comments: int):
        self.author = author
        self.title = title
        self.text = text
        print(url)
        with reddit_screenshots(url) as screenshotter:
            self.post_screenshot = screenshotter.screenshot_post()
            self.comments: list[RedditComment] = [*itertools.islice(self._get_comments(screenshotter), maximum_comments)]

    @staticmethod
    def _get_comments(screenshotter: RedditScreenshotter) -> Iterator[RedditComment]:
        for i in itertools.count():
            comment_locator = screenshotter.page.locator("shreddit-comment").nth(i)
            if not comment_locator.count():
                screenshotter.page.mouse.wheel(0, 15000)
                for _ in range(100):
                    if comment_locator.count():
                        break
                else:
                    break
            if not comment_locator.is_visible():
                continue
            collapse_locator = comment_locator.locator("button#comment-fold-button[aria-expanded=true]")
            if collapse_locator.count():
                if not collapse_locator.is_visible():
                    continue
                collapse_locator.click()
                while collapse_locator.count():
                    pass
            body = ' '.join(comment_locator.locator("#-post-rtjson-content").first.locator("p").all_inner_texts())
            if not body or body.isspace() or not (30 <= len(body) <= 280):
                continue
            print("Comment:", body)
            yield RedditComment(screenshotter, comment_locator, body)
