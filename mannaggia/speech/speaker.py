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

import os
from pydub import AudioSegment
from pydub.playback import get_player_name
import subprocess
from tempfile import NamedTemporaryFile


class Speaker(object):
    def __init__(self) -> None:
        super().__init__()

    def play(self, audio: AudioSegment) -> None:
        with NamedTemporaryFile("w+b", suffix=".wav") as f:
            audio.export(f.name, "wav")
            devnull = open(os.devnull, "w")
            subprocess.call(
                [get_player_name(), "-nodisp", "-autoexit", "-hide_banner", f.name],
                stdout=devnull,
                stderr=devnull,
            )
