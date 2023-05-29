from __future__ import annotations
from .track import Track


class TextTrack(Track):

    def __init__(self, text: str) -> None:
        super().__init__()
        self.text = text

    def position(self, *, x, y, relative) -> TextTrack:
        pass

    def start_at(self, time: float) -> TextTrack:
        pass

    def lasts(self, duration: float):
        pass
