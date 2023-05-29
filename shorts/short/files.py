import atexit
import os
import tempfile
from io import BytesIO
from typing import IO

_temporary_files: list[IO] = []


class TemporaryFile:
    def __init__(self, bytes_io: BytesIO):
        global _temporary_files
        with tempfile.NamedTemporaryFile("wb", delete=False) as backing:
            _temporary_files.append(backing)
            backing.write(bytes_io.read())
            self.name = str(backing.name)


@atexit.register
def __cleanup():
    for file in _temporary_files:
        os.remove(file.name)
