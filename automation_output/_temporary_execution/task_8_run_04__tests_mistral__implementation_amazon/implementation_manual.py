import unicodedata
import re

def slugify_manual(text, separator='-', lowercase=True, ignore=None, truncate=None):
    if not isinstance(text, str) or not isinstance(separator, str):
        return None

    if ignore is None:
        ignore = []
    if not isinstance(ignore, (list, tuple)):
        ignore = [ignore]

    try:
        text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii')
    except UnicodeDecodeError:
        return None

    for char in ignore:
        if isinstance(char, int):
            text = text.replace(chr(char), char)
        elif isinstance(char, str):
            text = text.replace(char, '')

    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', separator, text)

    if lowercase:
        text = text.lower()

    if truncate is not None and len(text) > truncate:
        text = text[:truncate]

    if not text.strip():
        return None

    return text
