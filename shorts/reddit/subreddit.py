import atexit
import itertools
import os
from typing import Generator
from praw import Reddit
from .credentials import RedditCredentials
from .submission import RedditSubmission

with open("seen.txt", "r") as f:
    _seen_posts = set(f.read().splitlines())


@atexit.register
def _save_seen_posts():
    os.remove("seen.txt")
    with open("seen.txt", "w") as f:
        f.write('\n'.join(_seen_posts))


class Subreddit:
    def __init__(self, name: str, credentials: RedditCredentials, maximum_submissions: int,
                 maximum_comments_per_submission: int):
        self.name = name
        self.reddit = Reddit(**credentials.credentials)
        self.subreddit = self.reddit.subreddit(self.name)
        self.submissions = self._get_submissions(maximum_submissions, maximum_comments_per_submission)

    def _get_submissions(self, limit: int,
                         maximum_comments_per_submission: int) -> Generator[RedditSubmission, None, None]:
        found = 0
        for submission in itertools.islice(self.subreddit.hot(limit=1024), 10, 100000):
            if submission.over_18 or submission.id in _seen_posts:
                continue
            _seen_posts.add(submission.id)
            try:
                if submission.author.is_suspended:
                    continue
            except:
                pass
            if submission.author.is_mod or not submission.is_self:
                continue
            yield RedditSubmission(submission.url, submission.author, submission.title, submission.selftext,
                                   maximum_comments_per_submission)
            found += 1
            if found == limit:
                break
