import unicodedata
import re

def slugify_manual(text, separator='-', lowercase=True, ignore=None, truncate=None):
    if not isinstance(text, str) or not isinstance(separator, str) or not isinstance(lowercase, bool) or (ignore is not None and not isinstance(ignore, (str, list))):
        return None
    if ignore is None:
        ignore = []
    if not isinstance(ignore, list):
        ignore = [ignore]
    if truncate is not None and not isinstance(truncate, int) or truncate < 0:
        return None
    try:
        text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii')
    except UnicodeDecodeError:
        return None
    text = re.sub(r'\s+', separator, text)
    if lowercase:
        text = text.lower()
    for char in ignore:
        text = text.replace(char, char)
    text = re.sub(r'[^\w' + re.escape(separator) + ''.join(ignore) + r']', '', text)
    if truncate and len(text) > truncate:
        text = text[:truncate]
    if not re.match(r'^[\w' + re.escape(separator) + ''.join([re.escape(c) for c in ignore]) + r']+$', text):
        return None
    return text
