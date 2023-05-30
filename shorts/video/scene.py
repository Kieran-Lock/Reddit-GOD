from __future__ import annotations
from moviepy.video.VideoClip import VideoClip, ColorClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from .duration import Duration
from .track import Track, VisualTrack


class Scene:
    def __init__(self, *tracks: Track) -> None:
        super().__init__()
        self.tracks = tracks
        self.duration = Duration.UNDEFINED
        durations = [*filter(lambda it: it is not Duration.UNDEFINED, map(lambda it: it.get_duration(self), tracks))]
        if durations:
            self.duration = max(durations, key=lambda it: it.seconds)

    def _build(self) -> VideoClip:
        width = height = 0
        for track in self.tracks:
            if isinstance(track, VisualTrack):
                width = max(width, int(track.width))
                height = max(height, int(track.height))
        return CompositeVideoClip(
            [it._build(self) for it in self.tracks],
            size=(width, height)
        ).set_fps(30)
