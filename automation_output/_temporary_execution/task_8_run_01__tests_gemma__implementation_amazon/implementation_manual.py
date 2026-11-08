import unicodedata
import re

def slugify_manual(text, separator='-', lowercase=True, ignore=None, truncate=None):
    if not isinstance(text, str) or not isinstance(separator, str) or not isinstance(lowercase, bool) or (ignore is not None and not isinstance(ignore, (str, list))) or (truncate is not None and not isinstance(truncate, int) or truncate < 0):
        return None

    if not text.strip():
        return None

    if ignore is None:
        ignore = []

    if isinstance(ignore, str):
        ignore = [ignore]

    normalized = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii')
    normalized = re.sub(r'[^\w\s-]', '', normalized).replace(' ', separator)

    if lowercase:
        normalized = normalized.lower()

    for char in ignore:
        normalized = normalized.replace(separator + char, char)

    if truncate and len(normalized) > truncate:
        normalized = normalized[:truncate].rsplit(separator, 1)[0] + separator if separator in normalized[truncate:] else normalized[:truncate]

    normalized = re.sub(r'[-\s]+', separator, normalized).strip(separator)

    if not normalized:
        return None

    return normalized
