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
        ignore_chars = set(''.join(ignore))
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
            if len(truncated) > 0:
                last_sep = truncated.rfind(separator)
                last_space = truncated.rfind(' ')
                
                potential_cut = max(last_sep, last_space)
                
                if potential_cut != -1 and potential_cut < len(slug) - 1:
                    slug = truncated[:potential_cut].strip(separator)
                else:
                    slug = truncated.strip(separator)
            else:
                slug = ""

    if not slug or slug.strip() == "":
        return None

    final_slug = ""
    for char in slug:
        if char.isalnum() or char == separator or char in ignore_chars:
            final_slug += char
        elif char.isspace():
            if final_slug and final_slug[-1] != separator:
                final_slug += separator

    final_slug = final_slug.strip(separator)
    
    if not final_slug:
        return None
        
    return final_slug