import unicodedata
import re

def slugify_manual(text, separator='-', lowercase=True, ignore=None, truncate=None):
    if not isinstance(text, str) or not isinstance(separator, str) or not isinstance(lowercase, bool) or (ignore is not None and not isinstance(ignore, (str, list))):
        return None
    if ignore is None:
        ignore = []
    if isinstance(ignore, str):
        ignore = [ignore]
    if truncate is not None and not isinstance(truncate, int) or truncate < 0:
        return None
    try:
        text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii')
    except UnicodeDecodeError:
        return None
    text = re.sub(r'\s+', separator, text)
    for char in ignore:
        text = text.replace(char, char.lower() if lowercase else char.upper())
    if lowercase:
        text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9' + re.escape(separator) + ''.join(map(re.escape, ignore)) + ']', '', text)
    if truncate and len(text) > truncate:
        text = text[:truncate]
    if not text or all(c in ' \-' for c in text):
        return None
    return text
