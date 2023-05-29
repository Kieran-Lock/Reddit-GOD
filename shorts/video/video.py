from moviepy.video.compositing.concatenate import concatenate_videoclips


class Video:
    def __init__(self, fps: int, width: int, height: int, background: tuple[int, int, int]) -> None:
        self.fps = fps
        self.width = width
        self.height = height
        self.background = background
        self.scenes = []

    def add_scenes(self, *scenes) -> None:
        self.scenes += list(scenes)

    def save(self, path: str) -> None:
        concatenate_videoclips([*map(lambda scene: scene._build(), self.scenes)]).write_videofile(path)
