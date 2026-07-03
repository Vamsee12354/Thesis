import unicodedata
import re

def slugify_manual(text, separator='-', lowercase=True, ignore=None, truncate=None):
    if not isinstance(text, str):
        return None

    try:
        text = text.encode('utf-8').decode('utf-8')
    except UnicodeError:
        return None

    if ignore is None:
        ignore = []
    elif isinstance(ignore, str):
        ignore = [ignore]

    def transliterate(input_str):
        normalized = unicodedata.normalize('NFKD', input_str)
        return "".join([c for c in normalized if not unicodedata.combining(c)])

    processed_text = transliterate(text)

    if lowercase:
        processed_text = processed_text.lower()

    allowed_chars_pattern = r'[^a-zA-Z0-9' + re.escape(''.join(ignore)) + r'\s]'

    clean_chars = []
    for char in processed_text:
        if char in ignore:
            clean_chars.append(char)
        elif char.isalnum():
            clean_chars.append(char)
        elif char.isspace():
            clean_chars.append(' ')
        else:
            continue

    clean_text = "".join(clean_chars)
    words = clean_text.split()

    if not words:
        return None

    joined_text = separator.join(words)

    if truncate is not None and isinstance(truncate, int) and truncate > 0:
        if len(joined_text) <= truncate:
            final_slug = joined_text
        else:
            truncated_part = joined_text[:truncate]
            if len(joined_text) > truncate and not joined_text[truncate-1].isspace() and not joined_text[truncate].isspace():
                last_space = truncated_part.rfind(separator)
                if last_space!= -1:
                    final_slug = truncated_part[:last_space]
                else:
                    final_slug = truncated_part.rsplit(separator, 1)[0] if separator in truncated_part else ""
                    if not final_slug and not truncated_part.startswith(separator):
                         final_slug = ""
            else:
                final_slug = truncated_part.rstrip(separator)

            if not final_slug and len(words) > 0:
                final_slug = words[0]
                if len(final_slug) > truncate:
                    final_slug = final_slug[:truncate]

            final_slug = final_slug.strip(separator)

            if not final_slug:
                return None

            if truncate < len(words[0].replace(' ', '')) and len(words[0]) > truncate:
                 return words[0][:truncate]

            joined_text = final_slug

        final_slug = joined_text
    else:
        final_slug = joined_text

    if not final_slug:
        return None

    return final_slug.strip(separator)