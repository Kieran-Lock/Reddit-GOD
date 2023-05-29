from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional, Self, TYPE_CHECKING
from moviepy.video.VideoClip import VideoClip
from .duration import Duration
if TYPE_CHECKING:
    from .scene import Scene


class Track(ABC):
    def __init__(self):
        self.duration = Duration.UNDEFINED
        self.starts_at = 0
        self.ends_after = -1

    def _get_duration(self, scene: Scene) -> Duration:
        if self.duration is not Duration.UNDEFINED:
            return self.duration
        return self._duration_impl(scene)

    @abstractmethod
    def _duration_impl(self, scene: Scene) -> Duration:
        ...

    def start_at(self, time: float) -> Self:
        self.starts_at = time
        return self

    def truncated(self, after_seconds: float) -> Self:
        self.ends_after = after_seconds
        return self

    def _build(self, scene: Scene) -> VideoClip:
        clip = (
            self._make_clip()
            .set_duration(self._get_duration(scene).seconds)
            .set_start(self.starts_at)
        )
        if self.ends_after >= 0:
            clip = clip.set_end(self.starts_at + self.ends_after)
        return self._prepare_clip(clip)

    @abstractmethod
    def _make_clip(self) -> VideoClip:
        ...

    def _prepare_clip(self, clip: VideoClip) -> VideoClip:
        return clip


class VisualTrack(Track, ABC):
    def __init__(self):
        super().__init__()
        self.position = (0, 0)
        self.relative_position = False
        self.width = 0
        self.height = 0

    def size(self, *, width: Optional[float] = None, height: Optional[float] = None) -> Self:
        if not (width or height):
            raise NotImplementedError("Scale must take at least one of x and y")
        if width and not height:
            ratio = width / self.width
            self.width = width
            self.height = ratio * self.height
        elif height and not width:
            ratio = height / self.height
            self.height = height
            self.width = ratio * self.width
        else:
            self.width = width
            self.height = height
        return self

    def pos(self, *, x: int | str, y: int | str) -> Self:
        self.position = (x, y)
        self.relative_position = False
        return self

    def relative_pos(self, *, x: float, y: float) -> Self:
        self.position = (x, y)
        self.relative_position = True
        return self

    def _prepare_clip(self, clip: VideoClip) -> VideoClip:
        return (
            clip.set_position(self.position)
            .resize((self.width, self.height))
        )
