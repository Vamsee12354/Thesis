import re
import unicodedata

def slugify_manual(text, separator='-', lowercase=True, ignore=None, truncate=None):
    if not isinstance(text, str):
        return None

    if ignore is None:
        ignore = []
    elif isinstance(ignore, str):
        ignore = [ignore]

    normalized = unicodedata.normalize('NFKD', text)
    cleaned = []
    for char in normalized:
        if char in ignore:
            cleaned.append(char)
            continue
        category = unicodedata.category(char)
        if category == 'Zs':
            cleaned.append(' ')
        elif category.startswith('L') or category.startswith('N'):
            cleaned.append(char.lower() if lowercase else char)

    slug = ''.join(cleaned)
    slug = re.sub(r'[^\w\s-]', '', slug)
    slug = re.sub(r'[\s-]+', ' ', slug).strip()
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

    return slug if slug else None