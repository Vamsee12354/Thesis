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
    ascii_text = []
    for char in normalized_text:
        if char in ignore:
            ascii_text.append(char)
            continue
        if unicodedata.category(char) == 'Mn':
            continue
        ascii_char = char.encode('ascii', 'ignore').decode('ascii')
        if ascii_char:
            ascii_text.append(ascii_char.lower() if lowercase else ascii_char)
        else:
            ascii_text.append(char.lower() if lowercase else char)

    cleaned_text = ''.join(ascii_text)
    cleaned_text = re.sub(r'[^\w\s' + re.escape(''.join(ignore)) + ']', '', cleaned_text)
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
    slug = re.sub(r'\s', separator, cleaned_text)

    if not slug:
        return None

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
        if not slug:
            return None

    return slug