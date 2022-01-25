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

from .tts import AudioSegment, TtsClient, TtsError

import requests
from tempfile import NamedTemporaryFile


class GoogleTranslateTTS(TtsClient):
    def __init__(self) -> None:
        super().__init__()

    def get_speech(self, s: str) -> AudioSegment:
        """Get speech from google translator api"""
        try:
            response = requests.get(
                "http://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&q=%s&tl=it"
                % s
            ).content
            temp = NamedTemporaryFile("wb")
            temp.write(response)
            return AudioSegment.from_mp3(temp.name)
        except Exception as e:
            raise TtsError(e)
