import unicodedata
import re

def slugify_manual(text, separator='-', lowercase=True, ignore=None, truncate=None):
    if not isinstance(text, str) or not isinstance(separator, str) or not isinstance(lowercase, bool) or (ignore is not None and not isinstance(ignore, (str, list))):
        return None
    if not isinstance(truncate, int) or truncate < 0:
        return None
    if isinstance(ignore, str):
        ignore = [ignore]
    if not text.strip():
        return None
    try:
        text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii')
    except UnicodeEncodeError:
        return None
    if ignore:
        for char in ignore:
            if isinstance(char, str):
                text = text.replace(char, char)
    else:
        text = re.sub(r'[^\w\s-]', '', text)
    if lowercase:
        text = text.lower()
    text = re.sub(r'[-\s]+', separator, text)
    text = text.strip(separator)
    if truncate and len(text) > truncate:
        text = text[:truncate]
        if separator and text.endswith(separator):
            text = text[:-len(separator)]
    if not text:
        return None
    return text
