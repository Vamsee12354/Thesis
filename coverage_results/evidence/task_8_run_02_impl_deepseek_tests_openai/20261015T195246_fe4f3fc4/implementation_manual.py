import re
import unicodedata

def slugify_manual(text, separator="-", lowercase=True, ignore=None, truncate=None):
    if not isinstance(text, str) or not text.strip():
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
        category = unicodedata.category(char)[0]
        if category == 'L' or category == 'N':
            slug_chars.append(char)
        elif category == 'Z':
            slug_chars.append(' ')

    slug = ''.join(slug_chars)
    slug = re.sub(r'[^\w\s' + re.escape(''.join(ignore)) + ']', '', slug)
    slug = re.sub(r'\s+', ' ', slug).strip()
    slug = re.sub(r'\s', separator, slug)

    if lowercase:
        slug = slug.lower()

    if not slug:
        return None

    if truncate is not None and truncate > 0:
        parts = slug.split(separator)
        truncated_parts = []
        current_length = 0
        for part in parts:
            if current_length + len(part) + (1 if truncated_parts else 0) <= truncate:
                truncated_parts.append(part)
                current_length += len(part) + (1 if truncated_parts else 0)
            else:
                break
        slug = separator.join(truncated_parts)
        if not slug:
            return None

    return slug