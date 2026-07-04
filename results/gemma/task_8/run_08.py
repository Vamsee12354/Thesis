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
    current_word = []
    
    for char in processed_text:
        if char.isalnum() or char in ignore_chars:
            current_word.append(char)
        else:
            if current_word:
                result_chars.append("".join(current_word))
                current_word = []
    if current_word:
        result_chars.append("".join(current_word))

    if not result_chars:
        return None

    slug = separator.join(result_chars)

    if truncate is not None and isinstance(truncate, int) and truncate > 0:
        if len(slug) > truncate:
            truncated = slug[:truncate]
            last_sep = truncated.rfind(separator)
            if last_sep!= -1:
                slug = truncated[:last_sep]
            else:
                slug = truncated
    
    if not slug.strip() and not any(c in slug for c in ignore_chars):
        return None

    return slug.strip(separator)