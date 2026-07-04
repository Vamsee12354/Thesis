import unicodedata
import re

def slugify_manual(text, separator='-', lowercase=True, ignore=None, truncate=None):
    if not isinstance(text, str):
        return None

    try:
        text.encode('utf-8').decode('utf-8')
    except (UnicodeEncodeError, UnicodeDecodeError):
        return None

    if ignore is None:
        ignore_chars = set()
    elif isinstance(ignore, str):
        ignore_chars = set(ignore)
    elif isinstance(ignore, list):
        ignore_chars = set("".join(ignore))
    else:
        ignore_chars = set()

    def transliterate(s):
        normalized = unicodedata.normalize('NFKD', s)
        return "".join([c for c in normalized if not unicodedata.combining(c)])

    processed_text = transliterate(text)
    
    if lowercase:
        processed_text = processed_text.lower()

    result_chars = []
    for char in processed_text:
        if char in ignore_chars:
            result_chars.append(char)
        elif char.isalnum():
            result_chars.append(char)
        elif char.isspace():
            result_chars.append(' ')
        else:
            result_chars.append(' ')

    temp_str = "".join(result_chars)
    words = temp_str.split()
    
    if not words:
        return None

    slug = separator.join(words)

    if not slug:
        return None

    if truncate is not None and isinstance(truncate, int) and truncate > 0:
        if len(slug) > truncate:
            truncated = slug[:truncate]
            last_sep = truncated.rfind(separator)
            if last_sep!= -1 and last_sep > 0:
                slug = truncated[:last_sep]
            else:
                slug = truncated
            slug = slug.rstrip(separator)

    if not slug:
        return None

    return slug