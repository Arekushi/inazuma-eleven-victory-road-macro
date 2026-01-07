import re
import unicodedata


def to_snake_case(value: str) -> str:
    if not value:
        return ''

    value = unicodedata.normalize('NFKD', value)
    value = value.encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', value)
    value = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1_\2', value)
    value = re.sub(r'[^a-zA-Z0-9]+', '_', value)
    value = re.sub(r'_+', '_', value)
    value = value.strip('_')
    
    return value.lower()


def to_kebab_case(value: str) -> str:
    if not value:
        return ''

    value = unicodedata.normalize('NFKD', value)
    value = value.encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'([a-z0-9])([A-Z])', r'\1-\2', value)
    value = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1-\2', value)
    value = re.sub(r'[^a-zA-Z0-9]+', '-', value)
    value = re.sub(r'-+', '-', value)
    value = value.strip('-')
    
    return value.lower()
