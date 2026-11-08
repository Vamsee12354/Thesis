import re
import unicodedata

def slugify_manual(text, separator="-", lowercase=True, ignore=None, truncate=None):
    if not isinstance(text, str) or not text.strip():
        return None

    if ignore is None:
        ignore = []
    elif isinstance(ignore, str):
        ignore = [ignore]

    normalized = unicodedata.normalize('NFKD', text)
    slug = []
    for char in normalized:
        if char in ignore:
            slug.append(char)
            continue
        category = unicodedata.category(char)
        if category == 'Zs':
            slug.append(' ')
        elif category.startswith('L') or category.startswith('N'):
            slug.append(char)
        elif char == separator:
            slug.append(' ')

    slug = ''.join(slug)
    slug = re.sub(r'[^\w\s' + re.escape(separator) + ']', '', slug)
    slug = re.sub(r'[' + re.escape(separator) + '\s]+', ' ', slug).strip()
    slug = re.sub(r'\s', separator, slug)

    if lowercase:
        slug = slug.lower()

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