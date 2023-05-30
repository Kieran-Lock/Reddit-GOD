from __future__ import annotations

from typing import Self

from moviepy.audio.fx.volumex import volumex
from moviepy.video.VideoClip import VideoClip
from moviepy.video.io.VideoFileClip import VideoFileClip

from .duration import Duration
from .scene import Scene
from .track import VisualTrack


class VideoTrack(VisualTrack):
    def __init__(self, path: str) -> None:
        super().__init__()
        self.clip = VideoFileClip(path)
        self.width = self.clip.size[0]
        self.height = self.clip.size[1]

    def _duration_impl(self, scene: Scene) -> Duration:
        return Duration(self.clip.duration)

    def _make_clip(self) -> VideoClip:
        return self.clip

    def volume(self, multiplier: float) -> Self:
        self.clip = self.clip.set_audio(volumex(self.clip.audio, multiplier))
        return self

    def skip_to(self, time: float) -> Self:
        self.clip = self.clip.subclip(time)
        return self
