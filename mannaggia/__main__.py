#!/usr/bin/python3

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

from appdirs import user_config_dir
import click
import os.path
from random import shuffle
from sys import exit, maxsize
from typing import List, Optional, Dict


from .santi.factory import Factory as SantiFactory
from .santi.santo import Santo
from .speech.speaker import Speaker
from .speech.tts import TTSClient
from .speech.espeak import ESpeakTTS
from .speech.google_translate import GoogleTranslateTTS
from .speech.ispeech import ISpeechTTS
from .speech.macos_say import MacOsTTS
from .speech.mozilla import MozillaTTS
from .stats import Stats

MOZILLA_TTS_CONFIG_DIR = os.path.join(user_config_dir(), "tts/.models.json")


def get_santi(dictionary: str, params: Dict[str, Optional[str]]) -> List[Santo]:
    if dictionary == "local":
        return SantiFactory.make_santi_from_local()
    elif dictionary == "file":
        return SantiFactory.make_santi_from_file(params["file"])
    elif dictionary == "santiebeati.it":
        return SantiFactory.make_santi_from_santiebeati()
    else:
        raise NotImplementedError("Unknown santi backend %s" % dictionary)


def get_tts_engine(tts: str, params: Dict[str, Optional[str]]) -> TTSClient:
    """Get tts engine by name"""
    if tts == "espeak":
        return ESpeakTTS(params["voice"])
    elif tts == "google":
        return GoogleTranslateTTS()
    elif tts == "ispeech":
        return ISpeechTTS()
    elif tts == "mozilla":
        return MozillaTTS(
            params["model_name"], params["config_file"], params["vocoder_name"]
        )
    elif tts == "voice-over":
        return MacOsTTS()
    else:
        raise NotImplementedError("Unknown tts engine %s" % tts)


@click.command()
@click.option(
    "--amount",
    "-n",
    default=maxsize,
    help="Specify the amount of santi to call before terminating the program (default: till you've got enough)",
)
@click.option(
    "--dictionary",
    "-d",
    default="local",
    help="Specify the dictionary to get santi from. Default 'local'; available options: ['local', 'file', 'santiebeati.it']",
)
@click.option(
    "--dictionary_file",
    "-D",
    default=None,
    help="Specify the dictionary file (required if dictionary is 'file')",
)
@click.option(
    "--prefix",
    "-p",
    default="mannaggia a",
    help="Specify the string to prepend to the name of the santo. Mind that you can always curse or praise the santo. Default: 'mannaggia a'",
)
@click.option(
    "--tts",
    "-t",
    default="google",
    help="Specify text-to-speech engine. Default: 'google'; available options: ['google', 'espeak', 'ispeech', 'mozilla', 'voice-over']",
)
@click.option("--model_name", default=None, help="Specify model name for mozilla tts")
@click.option(
    "--vocoder_name", default=None, help="Specify vocoder name for mozilla tts"
)
@click.option(
    "--config_file",
    default=MOZILLA_TTS_CONFIG_DIR,
    help="Specify config file path for mozilla tts",
)
@click.option(
    "-v",
    "--voice",
    default=None,
    help="Specify voice (optional for some tts engines, such as espeak)",
)
def main(
    amount: int,
    dictionary: str,
    dictionary_file: Optional[str],
    prefix: str,
    tts: str,
    model_name: Optional[str],
    vocoder_name: Optional[str],
    config_file: Optional[str],
    voice: Optional[str],
) -> None:
    # get dictionary
    santi = get_santi(dictionary, {"file": dictionary_file})
    shuffle(santi)
    # make tts engine
    tts_params = {
        "config_file": config_file,
        "model_name": model_name,
        "vocoder_name": vocoder_name,
        "voice": voice,
    }
    tts_engine = get_tts_engine(tts, tts_params)
    speaker = Speaker()
    # init stats
    stats = Stats()
    # init dict cursor
    cursor = 0
    for _ in range(amount):
        try:
            santo = santi[cursor]
            text = "%s %s" % (prefix, santo.name)
            print(text)
            speech = tts_engine.get_speech(text)
            speaker.play(speech)
            # incr saint named
            stats.saint_named()
            # adjust cursor (rewind)
            cursor += 1
            if cursor >= len(santi):
                cursor = 0
        except KeyboardInterrupt:
            break
    # print stats
    print(
        "\nNamed %d saints in %d seconds (%f S/m)"
        % (stats.named, stats.elapsed, stats.saints_per_minute)
    )
    exit(0)


if __name__ == "__main__":
    main()
