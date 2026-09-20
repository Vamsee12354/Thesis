from unicodedata import normalize, category
import re

def slugify_manual(text, separator='-', lowercase=True, ignore=None, truncate=None):
    if not isinstance(text, str) or not text.strip():
        return None

    if ignore is None:
        ignore = []
    elif isinstance(ignore, str):
        ignore = [ignore]

    normalized_text = normalize('NFKD', text)
    slug_parts = []

    for char in normalized_text:
        if char in ignore:
            slug_parts.append(char)
        elif category(char).startswith('P') or category(char).startswith('S'):
            slug_parts.append(' ')
        elif category(char).startswith('Z') or category(char) == 'Cc':
            slug_parts.append(' ')
        else:
            slug_parts.append(char)

    cleaned_text = ''.join(slug_parts)
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()

    if not cleaned_text:
        return None

    slug = []
    for char in cleaned_text:
        if char.isalnum():
            slug.append(char)
        else:
            slug.append(' ')

    slug = ''.join(slug)
    slug = re.sub(r'\s+', separator, slug).strip(separator)

    if lowercase:
        slug = slug.lower()

    if truncate is not None:
        if truncate <= 0:
            return None
        words = slug.split(separator)
        truncated_words = []
        current_length = 0
        for word in words:
            if current_length + len(word) <= truncate:
                truncated_words.append(word)
                current_length += len(word) + len(separator)
            else:
                break
        slug = separator.join(truncated_words)
        if not slug:
            return None

    return slug if slug else None