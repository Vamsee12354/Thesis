import re
import unicodedata


def slugify_manual(text, separator='-', lowercase=True, ignore=None, truncate=None):
    try:
        if not isinstance(text, str):
            return None
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
            if 'LATIN' in name or 'GREEK' in name or 'CYRILLIC' in name:
                return unicodedata.normalize('NFKD', char).encode('ascii', 'ignore').decode('ascii')
            if char.isalnum():
                return char
            return ''

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
                cleaned_parts.append(part)

        cleaned_text = ''.join(cleaned_parts)
        cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
        if not cleaned_text:
            return None

        words = cleaned_text.split()
        if not words:
            return None

        if separator:
            slug = separator.join(words)
        else:
            slug = ''.join(words)

        if lowercase:
            slug = slug.lower()

        if truncate is not None and isinstance(truncate, int) and truncate > 0:
            if len(slug) <= truncate:
                return slug
            truncated_slug = ''
            for word in words:
                candidate = (truncated_slug + separator + word) if truncated_slug else word
                if len(candidate) > truncate:
                    break
                truncated_slug = candidate
            slug = truncated_slug
            if not slug:
                return None

        if all(c.isalnum() or c == separator or c in ignore_set for c in slug):
            return slug
        return None
    except Exception:
        return None