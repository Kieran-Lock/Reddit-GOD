# from __future__ import annotations
# from abc import ABC, abstractmethod
# from .video import Video
#
#
# class Width(ABC):
#     UNDEFINED: Width
#
#     @abstractmethod
#     def get_width(self, video: Video):
#         ...
#
# Width.UNDEFINED = Width()
#
# class Height(ABC):
#     UNDEFINED: Height
#
#     @abstractmethod
#     def get_height(self, video: Video):
#         ...
#
# Height.UNDEFINED = Height()
#
# class Relative(Width, Height):
#     def __init__(self, amount: float):
#         self.amount = amount
#
#     def get_width(self, video: Video):
#         return video.width * self.amount
#
#     def get_height(self, video: Video):
#         return video.height * self.amount
#
#
# class FillWidth(Width):
#     def get_width(self, video: Video):
#         return