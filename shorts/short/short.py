import itertools
import random
from io import BytesIO
from shorts.reddit import RedditCredentials, Subreddit
from shorts.short.video import make_scene
from shorts.tts import Speech, Voices
from shorts.video.composition import Composition
import unicodedata
import re

from shorts.video.scene import Scene
from shorts.video.video_track import VideoTrack


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
            try:
                yield submission.title, [(submission.post_screenshot, Speech(submission.title, narrator)),
                                         *[(comment.screenshot, Speech(comment.content, narrator)) for comment in
                                           submission.comments
                                           ]]
            except AttributeError:
                pass

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

    def create_video(self) -> Composition:
        video = Composition()
        bg = VideoTrack("background.mp4").volume(.1)
        fg = Composition()
        for image, speech in self.clips:
            fg.add_scenes(make_scene(image, speech.speech, .5))
        fg_length = fg.get_duration().seconds
        bg_length = bg.get_duration().seconds
        bg.skip_to(random.randint(0, int(bg_length - fg_length))).truncated(fg_length)
        video.add_scenes(Scene(bg, fg))
        return video

    def upload(self, save_path: str) -> None:
        self.short.save(save_path)
        print(self.title + " #reddit #funny")
        # upload(self.title, save_path, self.thumbnail)

    def play(self) -> None:
        return
