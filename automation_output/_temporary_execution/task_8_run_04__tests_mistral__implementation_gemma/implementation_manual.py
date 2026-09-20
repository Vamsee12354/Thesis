import unicodedata
import re

def slugify_manual(text, separator='-', lowercase=True, ignore=None, truncate=None):
    if not isinstance(text, str):
        return None

    if ignore is None:
        ignore_chars = set()
    elif isinstance(ignore, str):
        ignore_chars = set(ignore)
    elif isinstance(ignore, list):
        ignore_chars = set("".join(ignore))
    else:
        ignore_chars = set()

    try:
        normalized = unicodedata.normalize('NFKD', text)
    except Exception:
        return None

    result_chars = []
    
    for char in normalized:
        if char in ignore_chars:
            result_chars.append(char)
        elif char.isalnum():
            result_chars.append(char)
        elif char.isspace():
            result_chars.append(' ')
        else:
            continue

    slug = "".join(result_chars)

    if lowercase:
        slug = slug.lower()

    words = slug.split()
    
    if not words:
        return None

    slug = separator.join(words)

    if truncate is not None and isinstance(truncate, int) and truncate > 0:
        if len(slug) > truncate:
            truncated = slug[:truncate]
            last_sep = truncated.rfind(separator)
            if last_sep != -1:
                slug = truncated[:last_sep]
            else:
                slug = truncated
        
        if not slug:
            return None

    if not slug:
        return None

    return slug