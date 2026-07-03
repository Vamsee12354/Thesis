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
        ignore_chars = set("".join(ignore))
    else:
        ignore_chars = set()

    def transliterate(input_str):
        normalized = unicodedata.normalize('NFKD', input_str)
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
        elif char.isspace() or (not char.isalnum() and char not in ignore_chars):
            result_chars.append(' ')

    cleaned_text = "".join(result_chars)
    words = cleaned_text.split()

    if not words:
        return None

    slug_parts = []
    for word in words:
        clean_word = ""
        for char in word:
            if char.isalnum() or char in ignore_chars:
                clean_word += char
        if clean_word:
            slug_parts.append(clean_word)

    if not slug_parts:
        return None

    slug = separator.join(slug_parts)

    if not slug:
        return None

    if truncate is not None and isinstance(truncate, int) and truncate > 0:
        if len(slug) > truncate:
            truncated = slug[:truncate]
            last_sep_idx = truncated.rfind(separator)

            if last_sep_idx!= -1:
                slug = slug[:last_sep_idx]
            else:
                last_space_idx = truncated.rfind(' ')
                if last_space_idx!= -1:
                    slug = truncated[:last_space_idx]
                else:
                    slug = truncated

            if not slug:
                return None

    return slug