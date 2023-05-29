from __future__ import annotations


class Duration:
    UNDEFINED: Duration = None

    def __init__(self, seconds: float):
        if self.__class__.UNDEFINED is not None and seconds < 0:
            raise ValueError(f"Seconds must be positive, got {seconds}")
        self._seconds = seconds

    @property
    def seconds(self):
        if self is self.__class__.UNDEFINED:
            raise NotImplementedError("Duration is undefined")
        return self._seconds


Duration.UNDEFINED = Duration(-1)
