import re
import unicodedata


def slugify_manual(text, separator='-', lowercase=True, ignore=None, truncate=None):
    if not isinstance(text, str):
        return None
    if ignore is None:
        ignore_set = set()
    elif isinstance(ignore, str):
        ignore_set = set(ignore)
    elif isinstance(ignore, list):
        ignore_set = set(''.join(ignore))
    else:
        return None

    try:
        text = unicodedata.normalize('NFKD', text)
        text = text.encode('ascii', 'ignore').decode('ascii')
    except Exception:
        return None

    def preserve_ignore_chars(match):
        char = match.group(0)
        if char in ignore_set:
            return char
        return ''

    text = ''.join(c if c in ignore_set or c.isalnum() or c.isspace() else ' ' for c in text)
    text = re.sub(r'\s+', ' ', text).strip()
    if not text:
        return None

    words = []
    for word in text.split():
        if truncate is not None:
            if len(separator.join(words + [word])) > truncate:
                break
        words.append(word)

    if not words:
        return None

    slug = separator.join(words)
    if lowercase:
        slug = slug.lower()

    if truncate is not None and len(slug) > truncate:
        slug = slug[:truncate]
        if separator in slug:
            slug = slug[:slug.rfind(separator)]
        else:
            slug = ''

    if not slug:
        return None

    return slug