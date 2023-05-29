import itertools
from io import BytesIO
from shorts.reddit import RedditCredentials, Subreddit
from shorts.short.video import make_scene
from shorts.tts import Speech, Voices
from shorts.video.video import Video
import unicodedata
import re


def slugify(value, allow_unicode=False):
    """
    Taken from https://github.com/django/django/blob/master/django/utils/text.py
    Convert to ASCII if 'allow_unicode' is False. Convert spaces or repeated
    dashes to single dashes. Remove characters that aren't alphanumerics,
    underscores, or hyphens. Convert to lowercase. Also strip leading and
    trailing whitespace, dashes, and underscores.
    """
    value = str(value)
    if allow_unicode:
        value = unicodedata.normalize('NFKC', value)
    else:
        value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value.lower())
    return re.sub(r'[-\s]+', '-', value).strip('-_')


class ShortsBatch:
    def __init__(self, subreddit: str, submissions: int, comments_per_submission: int,
                 credentials: RedditCredentials, narrator: Voices):
        self.shorts = [Short(title, clips) for title, clips in itertools.islice(self.browse_reddit(
            subreddit, comments_per_submission, credentials, narrator, submissions), submissions)]

    @staticmethod
    def browse_reddit(subreddit: str, comments: int, credentials: RedditCredentials, narrator: Voices,
                      submissions: int):
        subreddit = Subreddit(subreddit, credentials, submissions, comments)
        for submission in subreddit.submissions:
            yield submission.title, [(submission.post_screenshot, Speech(submission.title, narrator)),
                                     *[(comment.screenshot, Speech(comment.content, narrator)) for comment in
                                       submission.comments
                                       ]]

    def upload(self):
        for short in self.shorts:
            short.upload(f"OutputVideos/{slugify(short.title)}.mp4")
            # shutil.copyfile("temp.mp4", f"\"OutputVideos/{short.title}.mp4\"")


class Short:
    def __init__(self, title: str, clips: list[tuple[BytesIO, Speech]]):
        self.title = title
        self.clips = clips
        self.short = self.create_video()
        self.thumbnail = self.clips[0][0]

    def create_video(self) -> Video:
        video = Video(30, 1080, 1920, (0, 0, 0))
        for image, speech in self.clips:
            video.add_scenes(make_scene(image, speech.speech, .5))
        return video

    def upload(self, save_path: str) -> None:
        self.short.save(save_path)
        # upload(self.title, save_path, self.thumbnail)

    def play(self) -> None:
        return
