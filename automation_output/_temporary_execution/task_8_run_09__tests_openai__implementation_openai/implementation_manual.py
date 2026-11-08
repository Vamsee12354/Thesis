import re
import unicodedata


def slugify_manual(text, separator='-', lowercase=True, ignore=None, truncate=None):
    if not isinstance(text, str):
        return None
    if ignore is None:
        ignore_set = set()
    elif isinstance(ignore, str):
        ignore_set = set(ignore)
    elif isinstance(ignore, list):
        ignore_set = set(''.join(ignore))
    else:
        return None

    try:
        text = unicodedata.normalize('NFKD', text)
        text = text.encode('ascii', 'ignore').decode('ascii')
    except Exception:
        return None

    def preserve_ignore_chars(match):
        ch = match.group(0)
        if ch in ignore_set:
            return ch
        return ''

    text = ''.join(ch if ch in ignore_set or ch.isalnum() or ch.isspace() else ' ' for ch in text)
    text = re.sub(r'\s+', ' ', text).strip()
    if not text:
        return None

    words = []
    for word in text.split():
        filtered_word = ''.join(ch if ch in ignore_set or ch.isalnum() else '' for ch in word)
        if filtered_word:
            words.append(filtered_word)

    if not words:
        return None

    if truncate is not None and isinstance(truncate, int) and truncate > 0:
        truncated_words = []
        length = 0
        sep_len = len(separator)
        for w in words:
            w_len = len(w)
            if truncated_words:
                if length + sep_len + w_len > truncate:
                    break
                length += sep_len + w_len
            else:
                if w_len > truncate:
                    break
                length += w_len
            truncated_words.append(w)
        words = truncated_words
        if not words:
            return None

    slug = separator.join(words)
    if lowercase:
        slug = slug.lower()
    if not slug:
        return None
    return slug