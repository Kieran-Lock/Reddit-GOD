from os import environ
from simple_youtube_api.Channel import Channel
from simple_youtube_api.LocalVideo import LocalVideo
from simple_youtube_api.YouTube import YouTubeVideo
from .summarizer import generate_summary


channel = Channel()
channel.login(
    environ.get("YOUTUBE_CLIENT_SECRETS_PATH"),
    environ.get("YOUTUBE_CREDENTIALS_PATH")
)


def upload(post_title: str, path: str) -> YouTubeVideo:
    video = LocalVideo(file_path=path)

    video.set_title(generate_summary(post_title))
    video.set_description(post_title)
    video.set_tags([
        "shorts",
        "reddit",
        "god",
        "trending",
        "funny",
        "ama",
        "today",
        "news",
        "top",
        "wow"
    ])
    video.set_category("entertainment")
    video.set_default_language("en-US")

    video.set_embeddable(True)
    video.set_license("creativeCommon")
    video.set_privacy_status("public")
    video.set_public_stats_viewable(True)
    video.set_made_for_kids(False)

    # with open("thumb.png", "wb") as thumb:
    #     thumb.write(thumbnail.read())
    # short.set_thumbnail_path("thumb.png")

    video = channel.upload_video(video)
    video.like()
    return video
