import re
import unicodedata


def normalize_passive_text(text: str) -> str:
    text = unicodedata.normalize('NFKD', text)
    text = ''.join(
        c for c in text
        if not unicodedata.combining(c)
    )

    text = text.replace('%', '')
    text = text.replace('+', '')

    text = text.replace('\n', ' ')
    text = text.replace('\r', ' ')
    text = re.sub(r'\s+', ' ', text)

    return text.strip().lower()


def resolve_value_placeholder(
    text: str,
    value: float
) -> str:
    value_str = str(int(value)) if value.is_integer() else str(value)
    return text.replace('{value}', value_str)
