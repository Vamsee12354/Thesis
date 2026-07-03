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

    if lowercase and isinstance(lowercase, bool):
        processed_text = processed_text.lower()
    elif not isinstance(lowercase, bool):
        processed_text = text

    result_chars = []
    current_word = []

    pattern = re.compile(r'[\w\s]')

    chars = list(processed_text)
    n = len(chars)
    i = 0

    final_parts = []
    temp_word = []

    while i < n:
        char = chars[i]

        if char in ignore_chars:
            temp_word.append(char)
        elif char.isalnum():
            temp_word.append(char)
        elif char.isspace():
            if temp_word:
                final_parts.append("".join(temp_word))
                temp_word = []
        else:
            if temp_word:
                final_parts.append("".join(temp_word))
                temp_word = []
        i += 1
    if temp_word:
        final_parts.append("".join(temp_word))

    clean_parts = []
    for part in final_parts:
        cleaned = ""
        for c in part:
            if c.isalnum() or c in ignore_chars:
                cleaned += c
        if cleaned:
            clean_parts.append(cleaned)

    if not clean_parts:
        return None

    slug = separator.join(clean_parts)

    if not slug:
        return None

    if truncate is not None and isinstance(truncate, int) and truncate > 0:
        if len(slug) > truncate:
            truncated = slug[:truncate]
            last_sep = truncated.rfind(separator)
            if last_sep!= -1:
                slug = truncated[:last_sep]
            else:
                slug = truncated

            if not slug:
                return None

    return slug