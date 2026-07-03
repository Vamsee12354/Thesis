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
        elif char.isspace():
            result_chars.append(' ')
        else:
            result_chars.append(' ')

    temp_str = "".join(result_chars)
    words = temp_str.split()

    if not words:
        return None

    joined = separator.join(words)

    clean_joined = ""
    for i, char in enumerate(joined):
        if char.isalnum() or char in ignore_chars:
            clean_joined += char
        elif i > 0 and i < len(joined) - 1 and joined[i-1]!= separator and joined[i+1]!= separator:
            if separator!= "":
                clean_joined += separator
        elif i == 0 or i == len(joined) - 1:
            continue
        else:
            if separator!= "" and (i == 0 or joined[i-1]!= separator):
                clean_joined += separator

    final_words = []
    for w in words:
        word_cleaned = ""
        for c in w:
            if c.isalnum() or c in ignore_chars:
                word_cleaned += c
            elif c.isspace():
                continue
        if word_cleaned:
            final_words.append(word_cleaned)

    if not final_words:
        return None

    slug = separator.join(final_words)

    if truncate is not None and isinstance(truncate, int) and truncate > 0:
        if len(slug) > truncate:
            truncated_slug = slug[:truncate]
            last_sep = truncated_slug.rfind(separator)
            if last_sep!= -1:
                slug = truncated_slug[:last_sep].rstrip(separator)
            else:
                slug = truncated_slug

    if not slug:
        return None

    return slug