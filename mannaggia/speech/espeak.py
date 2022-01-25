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
from typing import Optional


class ESpeakTTS(TTSClient):
    def __init__(self, voice: Optional[str]) -> None:
        super().__init__()
        self.__voice = voice

    def get_speech(self, s: str) -> AudioSegment:
        """Get speech via espeak command"""
        try:
            temp = NamedTemporaryFile("w", suffix=".wav")
            devnull = open(os.devnull, "w")
            args = ["espeak", "-w", temp.name]
            if self.__voice is not None:
                args.extend(["-v", self.__voice])
            args.append(s)
            subprocess.call(
                args,
                stdout=devnull,
                stderr=devnull,
            )
            return AudioSegment.from_wav(temp.name)
        except Exception as e:
            raise TTSError(e)
