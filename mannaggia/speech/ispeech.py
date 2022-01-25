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

from os import unlink
import requests
from tempfile import NamedTemporaryFile
from urllib.parse import quote


class ISpeechTTS(TTSClient):
    def __init__(self) -> None:
        super().__init__()

    def get_speech(self, s: str) -> AudioSegment:
        """Get speech from ispeech api"""
        try:
            response = requests.get(
                "http://www.ispeech.org/p/generic/getaudio?text=%s%%2C&voice=euritalianmale&speed=0&action=convert"
                % quote(s)
            ).content
            with NamedTemporaryFile(delete=False) as temp:
                temp.write(response)
                temp.close()
                audio = AudioSegment.from_mp3(temp.name)
            unlink(temp.name)
            return audio
        except Exception as e:
            raise TTSError(e)
