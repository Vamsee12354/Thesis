import unicodedata
import re

def slugify_manual(text, separator='-', lowercase=True, ignore=None, truncate=None):
    if not isinstance(text, str) or not isinstance(separator, str) or not isinstance(lowercase, bool) or (ignore is not None and not isinstance(ignore, (str, list))):
        return None
    if ignore is None:
        ignore = []
    if isinstance(ignore, str):
        ignore = [ignore]
    try:
        text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii')
    except UnicodeDecodeError:
        return None
    text = re.sub(r'[^\w\s-]', '', text)
    if lowercase:
        text = text.lower()
    for char in ignore:
        text = text.replace(char, char)
    text = re.sub(r'[-\s]+', separator, text)
    if truncate is not None and len(text) > truncate:
        text = text[:truncate]
        if separator in text[-len(separator):]:
            text = text[:text.rfind(separator)]
    if not text.strip(separator):
        return None
    return text
