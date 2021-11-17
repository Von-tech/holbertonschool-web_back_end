#!/usr/bin/env python3
""" Creating module to complete series of tasks """


from typing import List
import re
import logging
PII_FIELDS = ("name", "email", "phone", "ssn", "password")


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ Creating an instance of class above """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = list(fields)

    def format(self, record: logging.LogRecord) -> str:
        """ Formats the record - self.FORMAT """
        return filter_datum(
            self.fields, self.REDACTION, super().format(record),
            self.SEPARATOR)


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """ Returns the log message obfuscated """
    for field in fields:
        message = re.sub(
            f"(?<={field}=).*?(?={separator})", redaction, message)
    return message


def get_logger() -> logging.Logger:
    """ Returns a Logger object """
    user_log = logging.getLogger('user_data')
    user_log.setLevel(logging.INFO)
    user_log.propagate = False
    user_log = logging.StreamHandler()
    user_log.setFormatter(RedactingFormatter(list(PII_FIELDS)))
    user_log.addHandler(user_log)
    return user_log
