"""
            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
                    Version 2, December 2004
 Copyright (C) 2022 Christian "veeso" Visintin
 Everyone is permitted to copy and distribute verbatim or modified
 copies of this license document, and changing it is allowed as long
 as the name is changed.
            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
  0. You just DO WHAT THE FUCK YOU WANT TO.
"""

from .tts import AudioSegment, TTSClient, TTSError

import os
import subprocess
from tempfile import NamedTemporaryFile


class MacOsTTS(TTSClient):
    def __init__(self) -> None:
        super().__init__()

    def get_speech(self, s: str) -> AudioSegment:
        """Get speech with macos `say` command"""
        try:
            temp = NamedTemporaryFile("w", suffix=".aiff")
            devnull = open(os.devnull, "w")
            subprocess.call(
                ["say", "-v", "Alice", "-o", temp.name, s],
                stdout=devnull,
                stderr=devnull,
            )
            return AudioSegment.from_file(temp.name)
        except Exception as e:
            raise TTSError(e)
