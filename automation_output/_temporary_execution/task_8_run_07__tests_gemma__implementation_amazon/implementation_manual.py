import unicodedata
import re

def slugify_manual(text, separator='-', lowercase=True, ignore=None, truncate=None):
    if not isinstance(text, str) or not isinstance(separator, str):
        return None
    if ignore is None:
        ignore = []
    if not isinstance(ignore, (list, tuple)):
        ignore = [ignore]
    if truncate is not None and not isinstance(truncate, int) or truncate < 0:
        return None
    try:
        text_bytes = text.encode('utf-8')
    except UnicodeEncodeError:
        return None
    text = unicodedata.normalize('NFKD', text_bytes.decode('utf-8')).encode('ascii', 'ignore').decode('ascii')
    for char in ignore:
        text = text.replace(char, char.lower() if lowercase else char)
    for char in ".,!?:;-":
        text = text.replace(char, ''if char in ignore else separator if char =='' else '')
    words = re.findall(r'\w+', text)
    if not words:
        return None
    slug = separator.join(words)
    if lowercase:
        slug = slug.lower()
    if truncate and len(slug) > truncate:
        slug = slug[:truncate]
    if not all(c.isalnum() or c == separator for c in slug):
        return None
    return slug
