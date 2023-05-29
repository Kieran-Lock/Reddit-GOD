import itertools
from typing import Generator
from praw import Reddit
from .credentials import RedditCredentials
from .submission import RedditSubmission


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
        for submission in itertools.islice(self.subreddit.hot(), 10, 100000):
            if submission.over_18:
                continue
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
