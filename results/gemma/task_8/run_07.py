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
    current_word = []

    allowed_alphanumeric = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")

    for char in processed_text:
        if char in ignore_chars:
            result_chars.append(char)
        elif char.isalnum():
            result_chars.append(char)
        elif char.isspace():
            result_chars.append(' ')
        else:
            result_chars.append(' ')

    slug_base = "".join(result_chars)
    words = slug_base.split()

    if not words:
        return None

    final_words = []
    for word in words:
        clean_word = ""
        for char in word:
            if char.isalnum() or char in ignore_chars:
                clean_word += char
        if clean_word:
            final_words.append(clean_word)

    if not final_words:
        return None

    slug = separator.join(final_words)

    if truncate is not None and isinstance(truncate, int) and truncate > 0:
        if len(slug) > truncate:
            truncated = slug[:truncate]
            if len(truncated) > 0 and truncated[-1] == separator[0] if separator else False:
                truncated = truncated.rstrip(separator)

            last_sep_idx = truncated.rfind(separator)
            if last_sep_idx!= -1:
                slug = truncated[:last_sep_idx]
            else:
                parts = slug.split(separator)
                temp_slug = ""
                for p in parts:
                    if len(temp_slug) + len(p) + len(separator) <= truncate:
                        temp_slug = (temp_slug + separator + p).strip(separator) if temp_slug else p
                    else:
                        break
                slug = temp_slug if temp_slug else truncated[:truncate]

            slug = slug.strip(separator)
            if not slug:
                return None

    return slug