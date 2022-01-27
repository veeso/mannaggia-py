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

from time import time


class Stats(object):
    """Santi stats"""

    def __init__(self) -> None:
        self.__named = 0
        self.__started = time()

    @property
    def named(self) -> int:
        return self.__named

    @property
    def saints_per_minute(self) -> float:
        minutes_elapsed = (time() - self.__started) // 60
        return self.__named if minutes_elapsed == 0 else self.__named / minutes_elapsed

    @property
    def elapsed(self) -> int:
        """Elapsed seconds since begin"""
        return int(time() - self.__started)

    def saint_named(self) -> None:
        """Increment named saint by one"""
        self.__named += 1
