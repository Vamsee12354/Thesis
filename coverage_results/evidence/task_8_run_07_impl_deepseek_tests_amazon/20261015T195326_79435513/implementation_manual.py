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
            ascii_char = char.encode('ascii', 'ignore').decode('ascii')
            if ascii_char:
                ascii_text.append(ascii_char.lower() if lowercase else ascii_char)
            else:
                ascii_text.append(char.lower() if lowercase else char)
        elif char.isspace():
            ascii_text.append(' ')
        else:
            if char in ignore:
                ascii_text.append(char)

    slug = ''.join(ascii_text)
    slug = re.sub(r'[^\w\s' + re.escape(''.join(ignore)) + ']', '', slug)
    slug = re.sub(r'\s+', ' ', slug).strip()
    slug = re.sub(r'\s', separator, slug)
    slug = re.sub(re.escape(separator) + '+', separator, slug)

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