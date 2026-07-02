import re
import unicodedata

def slugify_manual(text, separator='-', lowercase=True, ignore=None, truncate=None):
    if not isinstance(text, str) or not text.strip():
        return None

    if ignore is None:
        ignore = []
    elif isinstance(ignore, str):
        ignore = [ignore]

    preserved_chars = set()
    for char in ignore:
        preserved_chars.add(char)

    slug = []
    for char in text:
        if char in preserved_chars:
            slug.append(char)
            continue

        normalized = unicodedata.normalize('NFKD', char)
        stripped = normalized.encode('ascii', 'ignore').decode('ascii')
        if stripped:
            char = stripped

        if char.isalnum():
            slug.append(char.lower() if lowercase else char)
        elif char.isspace() or char == separator:
            slug.append(' ')

    slug = ''.join(slug)
    slug = re.sub(r'\s+', ' ', slug).strip()
    slug = re.sub(r'[^\w\s{}]'.format(re.escape(separator)), '', slug)
    slug = re.sub(r'\s', separator, slug)

    if not slug:
        return None

    if truncate is not None and truncate > 0:
        parts = slug.split(separator)
        truncated = []
        length = 0
        for part in parts:
            if length + len(part) + (1 if truncated else 0) <= truncate:
                truncated.append(part)
                length += len(part) + (1 if truncated else 0)
            else:
                break
        slug = separator.join(truncated)
        if not slug:
            return None

    return slug