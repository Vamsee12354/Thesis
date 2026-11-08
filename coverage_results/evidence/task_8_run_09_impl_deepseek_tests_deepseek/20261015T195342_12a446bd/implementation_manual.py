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
    ascii_text = []
    for char in normalized:
        if char in ignore:
            ascii_text.append(char)
            continue
        category = unicodedata.category(char)
        if category == 'Mn':
            continue
        if char.isalnum():
            ascii_text.append(char)
        else:
            ascii_text.append(' ')

    cleaned_text = ''.join(ascii_text)
    cleaned_text = re.sub(r'[^\w\s' + re.escape(''.join(ignore)) + ']', '', cleaned_text)
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()

    if not cleaned_text:
        return None

    slug = re.sub(r'\s+', separator, cleaned_text)

    if lowercase:
        slug = slug.lower()

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