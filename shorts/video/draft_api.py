from io import BytesIO
from .composition import Composition
from .audio_track import AudioTrack
from .image_track import ImageTrack
from .text_track import TextTrack
from .scene import Scene


video = Composition(30, 1080, 1920, (0, 0, 0))

video_track = ImageTrack(BytesIO())
audio_track = AudioTrack("audio.mp3").start_at(0.5)
text_track = TextTrack("Epic Text").position(x=0.5, y=0.1, relative=True)

scene = Scene(video_track, audio_track, text_track)
