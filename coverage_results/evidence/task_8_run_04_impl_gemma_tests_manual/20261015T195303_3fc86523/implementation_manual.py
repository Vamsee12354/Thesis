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
        text = text.encode('utf-8').decode('utf-8')
    except (UnicodeEncodeError, UnicodeDecodeError):
        return None

    def transliterate(s):
        res = []
        for char in s:
            if char in ignore_chars:
                res.append(char)
                continue
            
            normalized = unicodedata.normalize('NFKD', char)
            ascii_part = "".join([c for c in normalized if not unicodedata.combining(c)])
            
            if ascii_part:
                res.append(ascii_part)
            elif char.isalnum():
                res.append(char)
            elif char.isspace():
                res.append(" ")
            else:
                res.append(" ")
        return "".join(res)

    processed_text = transliterate(text)
    
    if lowercase:
        processed_text = processed_text.lower()

    words = []
    current_word = ""
    
    for char in processed_text:
        if char in ignore_chars:
            current_word += char
        elif char.isalnum():
            current_word += char
        else:
            if current_word:
                words.append(current_word)
                current_word = ""
    if current_word:
        words.append(current_word)

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
                
    if not slug and not any(c in slug for c in ignore_chars):
        return None
        
    return slug if slug else None