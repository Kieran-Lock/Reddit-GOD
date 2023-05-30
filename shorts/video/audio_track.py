from __future__ import annotations

from io import BytesIO

from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.video.VideoClip import VideoClip, ColorClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip

from .duration import Duration
from .scene import Scene
from .track import Track
from ..short.files import TemporaryFile


class AudioTrack(Track):
    def __init__(self, audio: BytesIO) -> None:
        super().__init__()
        self.audio = AudioFileClip(TemporaryFile(audio).name)

    def _duration_impl(self, scene: Scene) -> Duration:
        return Duration(self.audio.duration)

    def _make_clip(self) -> VideoClip:
        dummy = ColorClip((1, 1), color=(0, 0, 0))
        dummy = dummy.set_mask(ColorClip((1, 1), color=(0, 0, 0), ismask=True))
        return dummy.set_duration(self.audio.duration).set_audio(self.audio)
