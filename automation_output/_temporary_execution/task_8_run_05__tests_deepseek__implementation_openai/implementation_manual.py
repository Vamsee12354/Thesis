import re
import unicodedata


def slugify_manual(text, separator='-', lowercase=True, ignore=None, truncate=None):
    if not isinstance(text, str):
        return None
    if ignore is None:
        ignore = []
    elif isinstance(ignore, str):
        ignore = [ignore]
    try:
        text = text.encode('utf-8').decode('utf-8')
    except Exception:
        return None
    ignore_set = set(ignore)
    def transliterate(char):
        if char in ignore_set:
            return char
        if char.isalnum():
            return char
        try:
            name = unicodedata.name(char)
        except ValueError:
            return ''
        decomp = unicodedata.normalize('NFKD', char)
        ascii_equiv = ''.join(c for c in decomp if unicodedata.category(c) != 'Mn')
        ascii_equiv = ascii_equiv.encode('ascii', 'ignore').decode('ascii')
        return ascii_equiv
    text = ''.join(transliterate(c) for c in text)
    if not text:
        return None
    pattern_ignore = ''.join(re.escape(c) for c in ignore_set)
    pattern = f'[^\\w{pattern_ignore}]+'
    text = re.sub(pattern, separator, text)
    text = re.sub(f'{re.escape(separator)}+', separator, text)
    text = text.strip(separator)
    if lowercase:
        text = text.lower()
    if truncate is not None and isinstance(truncate, int) and truncate > 0:
        if len(text) <= truncate:
            return text if text else None
        parts = text.split(separator)
        truncated_parts = []
        length = 0
        for part in parts:
            part_len = len(part)
            if truncated_parts:
                if length + 1 + part_len > truncate:
                    break
                length += 1 + part_len
            else:
                if part_len > truncate:
                    break
                length += part_len
            truncated_parts.append(part)
        text = separator.join(truncated_parts)
        if not text:
            return None
    return text if text else None