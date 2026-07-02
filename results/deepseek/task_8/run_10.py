import re
import unicodedata

def slugify_manual(text, separator='-', lowercase=True, ignore=None, truncate=None):
    if not isinstance(text, str):
        return None

    if ignore is None:
        ignore = []
    elif isinstance(ignore, str):
        ignore = [ignore]

    text = text.strip()
    if not text:
        return None

    preserved_chars = set()
    for char in ignore:
        preserved_chars.update(char)

    slug_parts = []
    current_part = []

    for char in text:
        normalized_char = unicodedata.normalize('NFKD', char)
        normalized_char = ''.join([c for c in normalized_char if not unicodedata.combining(c)])

        if char in preserved_chars:
            if current_part:
                slug_parts.append(''.join(current_part))
                current_part = []
            slug_parts.append(char)
            continue

        if normalized_char.isalnum():
            current_part.append(normalized_char.lower() if lowercase else normalized_char)
        elif current_part:
            slug_parts.append(''.join(current_part))
            current_part = []

    if current_part:
        slug_parts.append(''.join(current_part))

    slug = []
    for part in slug_parts:
        if part in preserved_chars:
            slug.append(part)
        else:
            if slug and slug[-1] not in preserved_chars:
                slug.append(separator)
            slug.append(part)

    slug = ''.join(slug)
    slug = re.sub(f'{re.escape(separator)}+', separator, slug)
    slug = slug.strip(separator)

    if not slug:
        return None

    if truncate is not None and truncate > 0:
        if len(slug) > truncate:
            truncated_slug = slug[:truncate]
            if truncated_slug[-1] == separator:
                truncated_slug = truncated_slug[:-1]
            elif separator in slug[truncate:]:
                next_sep_pos = slug[truncate:].find(separator)
                if next_sep_pos != -1:
                    truncated_slug = slug[:truncate + next_sep_pos].rstrip(separator)
            slug = truncated_slug

    if not slug:
        return None

    return slug