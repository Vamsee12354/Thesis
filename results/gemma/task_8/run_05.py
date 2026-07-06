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
        ignore_list = [ignore]
    else:
        ignore_list = list(ignore)

    def transliterate(s):
        normalized = unicodedata.normalize('NFKD', s)
        return "".join([c for c in normalized if not unicodedata.combining(c)])

    text = transliterate(text)

    if lowercase:
        text = text.lower()

    pattern = r'[^a-zA-Z0-9\s' + re.escape("".join(ignore_list)) + r']'
    text = re.sub(pattern, ' ', text)

    words = text.split()
    
    if not words:
        return None

    processed_words = []
    for word in words:
        clean_word = ""
        for char in word:
            if char.isalnum() or char in "".join(ignore_list):
                clean_word += char
            elif char in "".join(ignore_list):
                clean_word += char
        
        if clean_word:
            processed_words.append(clean_word)

    if not processed_words:
        return None

    result = separator.join(processed_words)

    if truncate is not None and truncate > 0:
        if len(result) > truncate:
            truncated = result[:truncate]
            last_sep = truncated.rfind(separator)
            if last_sep != -1:
                result = truncated[:last_sep]
            else:
                result = truncated
                
    if not result.strip() and not any(c.isalnum() or c in "".join(ignore_list) for c in result):
        return None

    return result