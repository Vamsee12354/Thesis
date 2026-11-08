import re
import unicodedata

def slugify_manual(text, separator="-", lowercase=True, ignore=None, truncate=None):
    if not isinstance(text, str) or not text.strip():
        return None

    if ignore is None:
        ignore = []

    normalized_text = unicodedata.normalize('NFKD', text)
    ascii_text = normalized_text.encode('ascii', 'ignore').decode('ascii')

    cleaned_text = []
    for char in ascii_text:
        if char.isalnum() or char in ignore:
            cleaned_text.append(char)
        elif char.isspace():
            cleaned_text.append(' ')

    cleaned_text = ''.join(cleaned_text)
    cleaned_text = re.sub(r'[^\w\s' + re.escape(''.join(ignore)) + ']', '', cleaned_text)
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()

    if not cleaned_text:
        return None

    slug = re.sub(r'\s+', separator, cleaned_text)

    if lowercase:
        slug = slug.lower()

    if truncate is not None and truncate > 0:
        parts = slug.split(separator)
        truncated_slug = []
        current_length = 0
        for part in parts:
            if current_length + len(part) + (1 if truncated_slug else 0) <= truncate:
                truncated_slug.append(part)
                current_length += len(part) + (1 if truncated_slug else 0)
            else:
                break
        slug = separator.join(truncated_slug)

    return slug if slug else None