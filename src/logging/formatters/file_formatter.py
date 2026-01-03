import logging
import re


class PipelineFileFormatter(logging.Formatter):
    TAG_RE = re.compile(r'\[/?[^\]]+\]')
    EMOJI_RE = re.compile(r':[a-zA-Z0-9_+-]+:')

    def format(self, record: logging.LogRecord) -> str:
        if getattr(record, '_blank_line', False):
            return ''
        
        message = super().format(record)
        message = self.TAG_RE.sub('', message)
        message = self.EMOJI_RE.sub('', message)
        return message.strip()
