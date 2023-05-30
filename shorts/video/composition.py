from moviepy.video.VideoClip import VideoClip
from moviepy.video.compositing.concatenate import concatenate_videoclips

from shorts.video.duration import Duration
from shorts.video.scene import Scene
from shorts.video.track import VisualTrack


class Composition(VisualTrack):
    def __init__(self, fps: int = 30) -> None:
        super().__init__()
        self.fps = fps
        self.scenes = []
        self.position = ("center", "center")

    def add_scenes(self, *scenes) -> None:
        self.scenes += list(scenes)

    def _duration_impl(self, scene: Scene) -> Duration:
        return Duration(sum(it.duration.seconds for it in self.scenes))

    def _make_clip(self) -> VideoClip:
        return concatenate_videoclips([*map(lambda scene: scene._build(), self.scenes)]).set_fps(self.fps)

    def save(self, path: str) -> None:
        self._make_clip().write_videofile(path)
