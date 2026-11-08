import unicodedata
import re

def slugify_manual(text, separator='-', lowercase=True, ignore=None, truncate=None):
    if not isinstance(text, str) or not isinstance(separator, str) or not isinstance(lowercase, bool) or (ignore is not None and not isinstance(ignore, (str, list))):
        return None
    if ignore is None:
        ignore = []
    if isinstance(ignore, str):
        ignore = [ignore]
    if not isinstance(truncate, (int, type(None))) or (truncate is not None and truncate <= 0):
        return None
    try:
        text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii')
    except UnicodeEncodeError:
        return None
    text = re.sub(r'[^\w\s-]', '', text)
    for char in ignore:
        text = text.replace(char, char.lower() if lowercase else char)
    text = re.sub(r'\s+', separator, text)
    if lowercase:
        text = text.lower()
    if truncate is not None and len(text) > truncate:
        text = text[:truncate]
        if separator in text:
            text = text[:text.rfind(separator)]
    text = re.sub(r'[^-\w]', '', text)
    if not text:
        return None
    return text
