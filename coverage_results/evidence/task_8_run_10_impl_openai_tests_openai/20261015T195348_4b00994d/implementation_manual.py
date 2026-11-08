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
        text = text.strip()
        if not text:
            return None
        ignore_set = set(ignore)
        normalized = []
        for char in text:
            if char in ignore_set:
                normalized.append(char)
            else:
                decomposed = unicodedata.normalize('NFKD', char)
                filtered = ''.join(c for c in decomposed if not unicodedata.combining(c))
                normalized.append(filtered)
        normalized_text = ''.join(normalized)
        normalized_text = normalized_text.lower() if lowercase else normalized_text
        pattern = f'[^{re.escape(separator)}a-z0-9{"".join(re.escape(c) for c in ignore_set)}]+'
        cleaned = re.sub(pattern, ' ', normalized_text)
        cleaned = re.sub(r'\s+', ' ', cleaned).strip()
        if not cleaned:
            return None
        words = cleaned.split()
        if not words:
            return None
        slug = separator.join(words)
        if truncate is not None and isinstance(truncate, int) and truncate > 0:
            if len(slug) <= truncate:
                return slug
            truncated_words = []
            length = 0
            for word in words:
                word_len = len(word)
                if truncated_words:
                    sep_len = len(separator)
                else:
                    sep_len = 0
                if length + sep_len + word_len > truncate:
                    break
                if truncated_words:
                    truncated_words.append(separator)
                    length += sep_len
                truncated_words.append(word)
                length += word_len
            slug = ''.join(truncated_words)
            if not slug:
                return None
        return slug
    except Exception:
        return None