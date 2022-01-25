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

from abc import ABCMeta, abstractmethod
from pydub import AudioSegment


class TTSError(Exception):
    """
    TTS Error
    """

    def __init__(self, message: str):
        self.message = message

    def __str__(self):
        return repr(self.message)

    def __repr__(self):
        return str(self.message)


class TTSClient(object):
    """TTS client to get speech for string"""

    __metaclass__ = ABCMeta

    @abstractmethod
    def get_speech(self, s: str) -> AudioSegment:
        """Get audio segment from string"""
        raise NotImplementedError
