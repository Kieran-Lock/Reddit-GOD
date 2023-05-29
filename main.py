import os
from shorts import RedditCredentials, Voices, ShortsBatch


SUBREDDIT_NAME = "AskReddit"
NUMBER_OF_SUBMISSIONS = 10
NUMBER_OF_COMMENTS = 5
CREDENTIALS = RedditCredentials(
    client_id=os.environ.get("CLIENT_ID"),
    client_secret=os.environ.get("CLIENT_SECRET"),
    user_agent=os.environ.get("USER_AGENT")
)
NARRATOR_VOICE = Voices.ENGLISH_US_MALE


if __name__ == "__main__":
    shorts = ShortsBatch(SUBREDDIT_NAME, NUMBER_OF_SUBMISSIONS, NUMBER_OF_COMMENTS, CREDENTIALS, NARRATOR_VOICE)
    shorts.upload()
