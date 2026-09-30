import re
import unicodedata


def slugify_manual(text, separator='-', lowercase=True, ignore=None, truncate=None):
    try:
        if not isinstance(text, str):
            return None
        if isinstance(separator, int):
            separator = chr(separator)
        if ignore is None:
            ignore = []
        elif isinstance(ignore, str):
            ignore = [ignore]
        ignore_set = set(ignore)

        def transliterate(char):
            if char in ignore_set:
                return char
            name = unicodedata.name(char, None)
            if name is None:
                return ''
            decomp = unicodedata.normalize('NFKD', char)
            ascii_chars = ''.join(c for c in decomp if ord(c) < 128 and c.isalnum())
            return ascii_chars

        text = ''.join(transliterate(c) for c in text)
        if not text:
            return None

        pattern_ignore = '|'.join(re.escape(i) for i in ignore_set) if ignore_set else None

        if pattern_ignore:
            parts = re.split(f'({pattern_ignore})', text)
        else:
            parts = [text]

        cleaned_parts = []
        for part in parts:
            if pattern_ignore and re.fullmatch(pattern_ignore, part):
                cleaned_parts.append(part)
            else:
                part = re.sub(r'[^\w\s]', '', part, flags=re.UNICODE)
                part = re.sub(r'\s+', ' ', part)
                cleaned_parts.append(part)

        cleaned_text = ''.join(cleaned_parts).strip()
        if not cleaned_text:
            return None

        words = []
        for part in cleaned_parts:
            if pattern_ignore and re.fullmatch(pattern_ignore, part):
                words.append(part)
            else:
                words.extend(part.split())

        if not words:
            return None

        if lowercase:
            words = [w.lower() for w in words]

        slug = separator.join(words)

        if truncate is not None and isinstance(truncate, int) and truncate > 0:
            if len(slug) <= truncate:
                return slug
            truncated_words = []
            length = 0
            for w in words:
                add_len = len(w) + (len(separator) if truncated_words else 0)
                if length + add_len > truncate:
                    break
                truncated_words.append(w)
                length += add_len
            if not truncated_words:
                return None
            slug = separator.join(truncated_words)

        if not slug or all(c == separator for c in slug):
            return None

        return slug
    except Exception:
        return None