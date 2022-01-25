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

try:
    from TTS.utils.manage import ModelManager
    from TTS.utils.synthesizer import Synthesizer
except ImportError:
    pass
from os import unlink
from tempfile import NamedTemporaryFile
from typing import Optional


class MozillaTTS(TTSClient):
    def __init__(
        self, model_name: str, config_path: str, vocoder_name: Optional[str]
    ) -> None:
        super().__init__()
        manager = ModelManager(config_path)
        # get model
        model_path, config_path, model_item = manager.download_model(model_name)
        # get vocoder
        vocoder_name = (
            model_item["default_vocoder"] if vocoder_name is None else vocoder_name
        )
        vocoder_path, vocoder_config_path, _ = manager.download_model(vocoder_name)
        # create synth
        self.__synth = Synthesizer(
            model_path,
            config_path,
            None,
            None,
            vocoder_path,
            vocoder_config_path,
            None,
            None,
            False,
        )

    def get_speech(self, s: str) -> AudioSegment:
        try:
            wav = self.__synth.tts(s)
            with NamedTemporaryFile(delete=False) as temp:
                temp.close()
                self.__synth.save_wav(wav, temp.name)
                audio = AudioSegment.from_wav(temp.name)
            unlink(temp.name)
            return audio
        except Exception as e:
            raise TTSError(e)
