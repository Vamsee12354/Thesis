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
        ignore_chars = set(''.join(ignore))
    else:
        ignore_chars = set()

    if lowercase is True:
        text = text.lower()
    elif lowercase is False:
        pass
    else:
        text = text.lower()

    normalized = unicodedata.normalize('NFKD', text)

    char_list = []
    for char in normalized:
        if char in ignore_chars:
            char_list.append(char)
            continue

        if char.isalnum():
            char_list.append(char)
        elif char.isspace():
            char_list.append(' ')
        else:
            continue

    temp_str = "".join(char_list)

    words = temp_str.split()
    if not words:
        return None

    result = separator.join(words)

    if truncate is not None and isinstance(truncate, int) and truncate > 0:
        if len(result) > truncate:
            truncated = result[:truncate]
            last_sep = truncated.rfind(separator)
            if last_sep!= -1 and last_sep > 0:
                result = truncated[:last_sep]
            else:
                result = truncated

    if not result.strip() and not any(c in result for c in ignore_chars):
        return None

    final_result = ""
    for char in result:
        if char.isalnum() or char in ignore_chars or char == separator or char == ':
            final_result += char
        else:
            continue

    final_result = final_result.replace(' ', separator)

    while separator + separator in final_result:
        final_result = final_result.replace(separator + separator, separator)

    final_result = final_result.strip(separator)

    if not final_result and not any(c in text for c in ignore_chars):
        return None

    return final_result