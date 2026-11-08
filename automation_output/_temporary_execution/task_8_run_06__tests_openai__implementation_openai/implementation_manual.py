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
        ascii_equiv = re.sub(r'[^a-zA-Z0-9]', '', ascii_equiv)
        return ascii_equiv
    text = ''.join(transliterate(c) for c in text)
    if not text:
        return None
    pattern = f'[^{re.escape(separator)}a-zA-Z0-9{"".join(re.escape(c) for c in ignore_set)}]+'
    text = re.sub(pattern, ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    if not text:
        return None
    words = text.split()
    if separator == '' or separator is None:
        slug = ''.join(words)
    else:
        slug = separator.join(words)
    if lowercase:
        slug = slug.lower()
    if truncate is not None and isinstance(truncate, int) and truncate > 0:
        if len(slug) <= truncate:
            return slug
        truncated = ''
        for word in words:
            candidate = truncated + (separator if truncated else '') + word if separator else truncated + word
            if len(candidate) > truncate:
                break
            truncated = candidate
        slug = truncated
        if not slug:
            return None
    if not slug or all(c == separator for c in slug):
        return None
    return slug