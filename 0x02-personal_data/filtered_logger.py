#!/usr/bin/env python3
""" Task 0: Write a function that returns the log message obfuscated """
from typing import List
import re


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """ Returns the log message obfuscated """
    for field in fields:
        message = re.sub(
            f"(?<={field}=).*?(?={separator})", redaction, message)
    return message
