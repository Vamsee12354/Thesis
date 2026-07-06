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
        ignore_list = []
    elif isinstance(ignore, str):
        ignore_list = list(ignore)
    else:
        ignore_list = list(ignore)

    normalized = unicodedata.normalize('NFKD', text)
    
    chars = []
    for char in normalized:
        if char.isalnum() or char in ignore_list or char == ' ':
            chars.append(char)
        elif char.isspace():
            chars.append(' ')
        else:
            continue
            
    slug_text = "".join(chars)

    if lowercase:
        slug_text = slug_text.lower()

    words = slug_text.split()
    
    if not words:
        return None

    processed_words = []
    for word in words:
        clean_word = ""
        for char in word:
            if char.isalnum() or char in ignore_list:
                clean_word += char
            elif char in ignore_list:
                clean_word += char
        if clean_word:
            processed_words.append(clean_word)

    if not processed_words:
        return None

    result = separator.join(processed_words)

    if truncate is not None and truncate > 0:
        if len(result) > truncate:
            truncated_part = result[:truncate]
            last_sep_idx = truncated_part.rfind(separator)
            
            if last_sep_idx != -1:
                result = truncated_part[:last_sep_idx].rstrip(separator)
            else:
                result = truncated_part

    if not result:
        return None

    return result