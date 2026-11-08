import unicodedata
import re

def slugify_manual(text, separator='-', lowercase=True, ignore=None, truncate=None):
    if not isinstance(text, str) or not isinstance(separator, str) or not isinstance(lowercase, bool) or (ignore is not None and not isinstance(ignore, (str, list))) or (truncate is not None and not isinstance(truncate, int) or truncate <= 0):
        return None

    if not text.strip():
        return None

    if ignore is None:
        ignore = []

    if isinstance(ignore, str):
        ignore = [ignore]

    normalized_text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii')
    normalized_text = re.sub(r'[^\w\s-]', '', normalized_text).replace(' ', separator)

    if lowercase:
        normalized_text = normalized_text.lower()

    for char in ignore:
        normalized_text = normalized_text.replace(f'-{char}-', f'-{char}-').replace(f'-{char}', char).replace(f'{char}-', char)

    if truncate and len(normalized_text) > truncate:
        normalized_text = normalized_text[:truncate]

    normalized_text = re.sub(rf'[{re.escape(separator)}]+', separator, normalized_text).strip(separator)

    if not normalized_text:
        return None

    return normalized_text
