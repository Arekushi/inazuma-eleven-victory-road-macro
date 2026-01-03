import logging
import re


class PipelineConsoleFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        if getattr(record, '_blank_line', False):
            return ''

        return super().format(record)
