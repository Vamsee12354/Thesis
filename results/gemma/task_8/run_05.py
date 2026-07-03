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

    def transliterate(input_str):
        normalized = unicodedata.normalize('NFKD', input_str)
        return "".join([c for c in normalized if not unicodedata.combining(c)])

    processed_text = transliterate(text)

    if lowercase:
        processed_text = processed_text.lower()

    pattern = re.compile(r'[^a-zA-Z0-9\s' + re.escape(''.join(ignore_chars)) + r']')
    cleaned_text = pattern.sub('', processed_text)

    words = cleaned_text.split()

    if not words:
        return None

    joined_slug = separator.join(words)

    if truncate is not None and truncate > 0:
        if len(joined_slug) <= truncate:
            result = joined_slug
        else:
            truncated = joined_slug[:truncate]
            last_sep = truncated.rfind(separator)
            if last_sep!= -1 and last_sep > 0:
                result = truncated[:last_sep]
            else:
                result = truncated
    else:
        result = joined_slug

    if not result.strip() and not any(c in result for c in ignore_chars):
        return None

    return result