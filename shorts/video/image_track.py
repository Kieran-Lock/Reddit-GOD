from __future__ import annotations

from io import BytesIO

import numpy as np
from PIL import Image
from moviepy.video.VideoClip import VideoClip, ImageClip

from .duration import Duration
from .scene import Scene
from .track import Track, VisualTrack


class ImageTrack(VisualTrack):
    def __init__(self, image: BytesIO) -> None:
        super().__init__()
        self.image = Image.open(image)
        self.width = self.image.width
        self.height = self.image.height

    def _duration_impl(self, scene: Scene) -> Duration:
        return scene.duration

    def _make_clip(self) -> VideoClip:
        return ImageClip(np.array(self.image))
