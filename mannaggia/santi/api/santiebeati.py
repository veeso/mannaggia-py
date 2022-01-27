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

from .client import Client, ClientError
from ..santo import Santo

import requests
import string
import random
import re
from typing import List, Optional, Any


class SantiEBeatiClient(Client):
    """www.santiebeati.it client"""

    def __init__(self) -> None:
        super().__init__()

    def query_santi(self, amount: int) -> List[Santo]:
        santi: List[Santo] = []
        regex = re.compile(r"<[^>]+>")
        while len(santi) < amount:
            santi.extend(self.__query_santi_by_random_letter(regex))
        return santi[:amount]

    def __query_santi_by_random_letter(self, regex: Any) -> List[Santo]:
        """Query santi by random alphabet letter"""
        letter = random.choice(string.ascii_uppercase)
        try:
            response = requests.get("http://www.santiebeati.it/%s" % letter).text
        except Exception as e:
            raise ClientError(e)
        result = []
        for line in response.splitlines():
            santo = self.__get_santo_name(line, regex)
            if santo:
                result.append(santo)
        return result

    def __get_santo_name(self, line: str, regex: Any) -> Optional[Santo]:
        """Get name of santo from a line of response"""
        start_offset = line.find("tit")
        if start_offset == -1:
            return None
        line = line[start_offset:]
        start_offset = line.find("<FONT")
        if start_offset == -1:
            return None
        line = line[start_offset:]
        end_offset = line.find("</b></FONT></a>")
        if end_offset == -1:
            return None
        line = line[:end_offset]
        return Santo(regex.sub("", line).strip())
