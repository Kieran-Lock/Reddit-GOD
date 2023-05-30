from __future__ import annotations

from io import BytesIO

from ..video.audio_track import AudioTrack
from ..video.image_track import ImageTrack
from ..video.scene import Scene

FPS = 30
WIDTH = 1080
HEIGHT = 1920


def make_scene(screenshot: BytesIO, audio: BytesIO, buffer: float) -> Scene:
    return Scene(
        AudioTrack(audio),
        ImageTrack(screenshot).pos(x="center", y="center").size(width=WIDTH*.9)
    )

# class RedditClip:
#     def __init__(self, audio: BytesIO, screenshot: BytesIO, buffer: float) -> None:
#         Video()
#         audio_file = TemporaryFile(audio).name
#         audio_clip = AudioFileClip(audio_file)
#         image_clip: ImageClip = (
#             ImageClip(array(Image.open(screenshot)))
#             .set_fps(30)
#             .set_position(("center", "center"))
#             .set_duration(audio_clip.duration)
#         )
#         image_clip = image_clip.resize((WIDTH, image_clip.size[1] / image_clip.size[0] * WIDTH))
#         color_clip = ColorClip((WIDTH, HEIGHT), col=(0, 0, 0))
#         still_clip = CompositeVideoClip([color_clip.set_duration(buffer), image_clip])
#         clip_with_audio = CompositeVideoClip(
#             [color_clip.set_duration(audio_clip.duration), image_clip.set_audio(audio_clip)])
#         self.clip = concatenate_videoclips(
#             [
#                 clip_with_audio,
#                 # still_clip
#             ]
#         )
#
#
# class Video:
#     def __init__(self, fps: int, background_colour: tuple[int, int, int]) -> None:
#         self.fps = fps
#         self.background_colour = background_colour
#         self.clips = []
#
#     def add_clip(self, reddit_screenshot: BytesIO, audio: BytesIO, buffer_duration: float) -> Video:
#         self.clips.append(RedditClip(audio, reddit_screenshot, buffer_duration).clip)
#         return self
#
#     def save(self, save_path: str) -> None:
#         concatenate_videoclips(self.clips).write_videofile(save_path)
