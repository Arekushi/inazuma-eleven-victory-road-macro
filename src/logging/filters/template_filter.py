import logging
from logging import LogRecord

from src.logging import TemplateRenderer


class TemplateFilter(logging.Filter):
    def filter(self, record: LogRecord) -> bool:
        context = self._extract_context(record)

        if context:
            try:
                record.msg = TemplateRenderer.render(
                    str(record.msg),
                    context
                )
                record.args = ()
            except Exception as e:
                record.msg = f"[Template error] {record.msg} ({e})"

        return True

    def _extract_context(self, record: LogRecord) -> dict:
        standard = logging.LogRecord(
            "", 0, "", 0, "", (), None
        ).__dict__.keys()

        return {
            k: v
            for k, v in record.__dict__.items()
            if k not in standard
        }
