import unicodedata
import re

def slugify_manual(text, separator="-", lowercase=True, ignore=None, truncate=None):
    if not isinstance(text, str):
        return None

    if ignore is None:
        ignore_chars = set()
    elif isinstance(ignore, str):
        ignore_chars = set(ignore)
    elif isinstance(ignore, list):
        ignore_chars = set(ignore)
    else:
        ignore_chars = set()

    try:
        text = unicodedata.normalize('NFKD', text)
    except Exception:
        return None

    def transliterate(char):
        if char in ignore_chars:
            return char
        if char.isalnum():
            return char
        return None

    processed_chars = []
    for char in text:
        res = transliterate(char)
        if res:
            processed_chars.append(res)
        elif not char.isspace() and char not in ignore_chars:
            if not char.isalnum():
                continue
        else:
            processed_chars.append(" ")

    temp_str = "".join(processed_chars)
    
    if lowercase:
        temp_str = temp_str.lower()

    words = temp_str.split()
    
    if not words:
        return None

    slug = separator.join(words)

    if truncate is not None and truncate > 0:
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

    final_chars = []
    for char in slug:
        if char.isalnum() or char == separator or char in ignore_chars:
            final_chars.append(char)
    
    result = "".join(final_chars)
    
    if not result:
        return None
        
    return result