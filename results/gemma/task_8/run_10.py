import unicodedata
import re

def slugify_manual(text, separator='-', lowercase=True, ignore=None, truncate=None):
    if not isinstance(text, str):
        return None

    try:
        text.encode('utf-8').decode('utf-8')
    except UnicodeError:
        return None

    if ignore is None:
        ignore_chars = set()
    elif isinstance(ignore, str):
        ignore_chars = set(ignore)
    elif isinstance(ignore, list):
        ignore_chars = set(ignore)
    else:
        ignore_chars = set()

    def transliterate(input_str):
        normalized = unicodedata.normalize('NFKD', input_str)
        return "".join([c for c in normalized if not unicodedata.combining(c)])

    processed_text = transliterate(text)

    if not ignore_chars:
        regex_pattern = r'[^a-zA-Z0-9\s' + re.escape(''.join(ignore_chars)) + r']'
        processed_text = re.sub(regex_pattern, ', processed_text)
    else:
        pattern = r'[^a-zA-Z0-9\s' + re.escape(''.join(ignore_chars)) + r']'
        processed_text = re.sub(pattern, ', processed_text)

    words = processed_text.split()

    if not words:
        return None

    slug_parts = []
    for word in words:
        clean_word = ""
        for char in word:
            if char.isalnum() or char in ignore_chars:
                clean_word += char
            elif char in ignore_chars:
                clean_word += char
        if clean_word:
            slug_parts.append(clean_word)

    if not slug_parts:
        return None

    result = separator.join(slug_parts)

    if not lowercase:
        pass
    else:
        result = result.lower()

    if truncate is not None and isinstance(truncate, int) and truncate > 0:
        if len(result) > truncate:
            truncated = result[:truncate]
            last_sep = truncated.rfind(separator)
            if last_sep!= -1:
                result = result[:last_sep]
            else:
                last_space = truncated.rfind(' ')
                if last_space!= -1:
                    result = truncated[:last_space]
                else:
                    result = truncated

            result = result.strip(separator)

            if not result and len(result) == 0:
                return None

    if not result:
        return None

    return result