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
            last_sep = truncated.rfind(separator)
            last_space = truncated.rfind(' ')
            
            best_split = max(last_sep, last_space)
            
            if best_split != -1 and best_split > 0:
                slug = slug[:best_split].strip(separator)
            else:
                slug = truncated.strip(separator)

    final_slug = slug.strip(separator)
    
    if not final_slug and not any(c in final_slug for c in ignore_chars):
        return None
        
    return final_slug if final_slug or any(c in text for c in ignore_chars) else None