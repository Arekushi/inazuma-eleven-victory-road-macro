from string import Template
from typing import Any, Mapping


class TemplateRenderer:
    @staticmethod
    def render(template_str: str, context: Mapping[str, Any]) -> str:
        return Template(template_str).safe_substitute(context)
