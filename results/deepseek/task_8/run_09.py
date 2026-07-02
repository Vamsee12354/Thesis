import re
import unicodedata

def slugify_manual(text, separator='-', lowercase=True, ignore=None, truncate=None):
    if not isinstance(text, str) or not text.strip():
        return None

    if ignore is None:
        ignore = []
    elif isinstance(ignore, str):
        ignore = [ignore]

    preserved_chars = set(ignore)

    normalized = unicodedata.normalize('NFKD', text)
    slug_parts = []

    for char in normalized:
        if char in preserved_chars:
            slug_parts.append(char)
            continue

        category = unicodedata.category(char)
        if category.startswith('L') or category.startswith('N'):
            slug_parts.append(char)
        elif category.startswith('Z'):
            slug_parts.append(' ')

    slug = ''.join(slug_parts)
    slug = re.sub(r'[^\w\s' + re.escape(''.join(preserved_chars)) + ']', '', slug)
    slug = re.sub(r'\s+', ' ', slug).strip()

    if not slug:
        return None

    if lowercase:
        slug = slug.lower()

    slug = re.sub(r'\s', separator, slug)

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