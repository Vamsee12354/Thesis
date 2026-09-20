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
        text = str(text, 'utf-8')
    except (TypeError, UnicodeDecodeError):
        return None
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii')
    for char in ignore:
        text = text.replace(char, char)
    for char in ".,!?;:()[]{}'\"/\\":
        text = text.replace(char, ' ' if char in ignore else '')
    text = re.sub(r'\s+','', text).strip()
    if not text:
        return None
    words = text.split()
    if lowercase:
        words = [word.lower() for word in words]
    joined_text = separator.join(words)
    if truncate is not None and len(joined_text) > truncate:
        joined_text = joined_text[:truncate]
    return joined_text
