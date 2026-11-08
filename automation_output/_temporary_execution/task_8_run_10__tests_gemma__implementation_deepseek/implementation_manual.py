import re
import unicodedata

def slugify_manual(text, separator="-", lowercase=True, ignore=None, truncate=None):
    if not text:
        return None

    if ignore is None:
        ignore = []

    if isinstance(ignore, str):
        ignore = [ignore]

    text = unicodedata.normalize('NFKD', text)
    text = text.encode('ascii', 'ignore').decode('ascii')

    cleaned_text = []
    for char in text:
        if char in ignore:
            cleaned_text.append(char)
        elif char.isalnum():
            cleaned_text.append(char)
        elif char.isspace():
            cleaned_text.append(separator)
        else:
            cleaned_text.append('')

    cleaned_text = ''.join(cleaned_text)
    cleaned_text = re.sub(f'[{re.escape(separator)}]+', separator, cleaned_text)
    cleaned_text = cleaned_text.strip(separator)

    if lowercase:
        cleaned_text = cleaned_text.lower()

    if truncate is not None and truncate > 0:
        words = cleaned_text.split(separator)
        truncated_text = []
        length = 0
        for word in words:
            if length + len(word) + (1 if truncated_text else 0) <= truncate:
                truncated_text.append(word)
                length += len(word) + (1 if truncated_text else 0)
            else:
                break
        cleaned_text = separator.join(truncated_text)

    if not cleaned_text:
        return None

    return cleaned_text