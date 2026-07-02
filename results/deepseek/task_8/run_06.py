import re
import unicodedata

def slugify_manual(text, separator='-', lowercase=True, ignore=None, truncate=None):
    if not isinstance(text, str):
        return None

    if ignore is None:
        ignore = []
    elif isinstance(ignore, str):
        ignore = [ignore]

    normalized_text = unicodedata.normalize('NFKD', text)
    slug_chars = []

    for char in normalized_text:
        if char in ignore:
            slug_chars.append(char)
            continue

        category = unicodedata.category(char)
        if category.startswith('L') or category.startswith('N'):
            slug_chars.append(char)
        elif category.startswith('Z'):
            slug_chars.append(' ')

    slug = ''.join(slug_chars)
    slug = re.sub(r'[^\w\s' + re.escape(''.join(ignore)) + ']', '', slug)
    slug = re.sub(r'\s+', ' ', slug).strip()

    if not slug:
        return None

    slug = re.sub(r'\s', separator, slug)

    if lowercase:
        slug = slug.lower()

    if truncate is not None and truncate > 0:
        parts = slug.split(separator)
        truncated = []
        current_length = 0

        for part in parts:
            if current_length + len(part) + (1 if truncated else 0) <= truncate:
                truncated.append(part)
                current_length += len(part) + (1 if truncated else 0)
            else:
                break

        slug = separator.join(truncated)
        if not slug:
            return None

    return slug