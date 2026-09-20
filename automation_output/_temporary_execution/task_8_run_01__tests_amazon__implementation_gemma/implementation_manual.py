import unicodedata
import re

def slugify_manual(text, separator='-', lowercase=True, ignore=None, truncate=None):
    if not isinstance(text, str):
        return None

    try:
        text = text.encode('utf-8').decode('utf-8')
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

    normalized = unicodedata.normalize('NFKD', text)
    
    chars = []
    for char in normalized:
        if char in ignore_chars:
            chars.append(char)
        elif char.isalnum():
            chars.append(char)
        elif char.isspace():
            chars.append(' ')
        else:
            continue
    
    processed_text = "".join(chars)

    if lowercase:
        processed_text = processed_text.lower()

    words = processed_text.split()
    
    if not words:
        return None

    slug = separator.join(words)

    if truncate is not None and isinstance(truncate, int) and truncate > 0:
        if len(slug) > truncate:
            truncated = slug[:truncate]
            last_sep_idx = truncated.rfind(separator)
            
            if last_sep_idx != -1:
                slug = truncated[:last_sep_idx].rstrip(separator)
            else:
                last_space_idx = truncated.rfind(' ')
                if last_space_idx != -1:
                    slug = truncated[:last_space_idx]
                else:
                    slug = truncated

    if not slug or slug.strip() == "":
        return None

    return slug