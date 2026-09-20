import unicodedata
import re

def slugify_manual(text, separator='-', lowercase=True, ignore=None, truncate=None):
    if not isinstance(text, str) or not isinstance(separator, str) or not isinstance(lowercase, bool) or (ignore is not None and not isinstance(ignore, (str, list))) or (truncate is not None and not isinstance(truncate, int) or truncate < 0):
        return None
    if not text.strip():
        return None
    if ignore is None:
        ignore = []
    if isinstance(ignore, str):
        ignore = [ignore]
    ignore = [c for c in ignore if isinstance(c, str)]
    text = ''.join(c for c in unicodedata.normalize('NFKD', text) if not unicodedata.combining(c) or c in ignore)
    for c in ignore:
        text = text.replace(c, c)
    if lowercase:
        text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'\s+', separator, text)
    if truncate and len(text) > truncate:
        text = text[:truncate]
        if separator in text[truncate-len(separator):]:
            text = text[:text.rfind(separator, 0, truncate)]
    text = re.sub(r'[-]{2,}', '-', text)
    if not text.strip(separator):
        return None
    return text
