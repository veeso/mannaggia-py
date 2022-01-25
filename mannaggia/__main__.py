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

import click
from random import shuffle
from sys import exit, maxsize
from typing import List


from .santi.factory import Factory as SantiFactory
from .santi.santo import Santo
from .speech.speaker import Speaker
from .speech.tts import TtsClient
from .speech.google_translate import GoogleTranslateTTS


def get_santi(dictionary: str) -> List[Santo]:
    return {
        "local": SantiFactory.make_santi_from_local,
        "santiebeati.it": SantiFactory.make_santi_from_santiebeati,
    }[dictionary]()


def get_tts_engine(tts: str) -> TtsClient:
    """Get tts engine by name"""
    return {
        "google": GoogleTranslateTTS(),
    }[tts]


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
    help="Specify the dictionary to get santi from. Default 'local'; available options: ['local', 'santiebeati.it']",
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
    help="Specify text-to-speech engine. Default: 'google'; available options: ['google']",
)
def main(amount: int, dictionary: str, prefix: str, tts: str) -> None:
    # get dictionary
    santi = get_santi(dictionary)
    shuffle(santi)
    tts_engine = get_tts_engine(tts)
    speaker = Speaker()
    cursor = 0
    for _ in range(amount):
        try:
            santo = santi[cursor]
            text = "%s %s" % (prefix, santo.name)
            print(text)
            speech = tts_engine.get_speech(text)
            speaker.play(speech)
            # adjust cursor (rewind)
            cursor += 1
            if cursor >= len(santi):
                cursor = 0
        except KeyboardInterrupt:
            exit(0)


if __name__ == "__main__":
    main()
