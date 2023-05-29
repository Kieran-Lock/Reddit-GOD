from moviepy.video.VideoClip import VideoClip, ColorClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from .duration import Duration
from .track import Track


class Scene:
    def __init__(self, width: int, height: int, *tracks: Track) -> None:
        self.width = width
        self.height = height
        self.tracks = tracks
        self.duration = Duration.UNDEFINED
        durations = [*filter(lambda it: it is not Duration.UNDEFINED, map(lambda it: it._get_duration(self), tracks))]
        if durations:
            self.duration = max(durations, key=lambda it: it.seconds)

    def _build(self) -> VideoClip:
        return CompositeVideoClip(
            [ColorClip((self.width, self.height), color=(0, 0, 0), duration=self.duration.seconds)] +
            [it._build(self) for it in self.tracks]
        ).set_fps(30)
