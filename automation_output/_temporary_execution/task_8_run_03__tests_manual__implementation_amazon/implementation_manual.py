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
    ignore = [i.lower() for i in ignore]
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8').strip()
    text = re.sub(r'[^\w\s-]', '', text)
    if lowercase:
        text = text.lower()
    for char in ignore:
        text = text.replace(char, char)
    text = re.sub(r'[-\s]+', separator, text)
    if truncate and len(text) > truncate:
        text = text[:truncate]
        if separator in text[-len(separator):]:
            text = text[:text.rfind(separator)]
    if not re.search(r'^[\w-]+$', text):
        return None
    return text
