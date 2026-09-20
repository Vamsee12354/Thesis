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
                part = re.sub(r'\s+', ' ', part, flags=re.UNICODE)
                cleaned_parts.append(part)

        cleaned_text = ''.join(cleaned_parts)
        cleaned_text = cleaned_text.strip()
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

        sep = separator if isinstance(separator, str) else chr(separator)
        slug_words = []
        length = 0
        for word in words:
            if truncate is not None:
                if length == 0:
                    if len(word) > truncate:
                        break
                    length = len(word)
                    slug_words.append(word)
                else:
                    if length + len(sep) + len(word) > truncate:
                        break
                    length += len(sep) + len(word)
                    slug_words.append(word)
            else:
                slug_words.append(word)

        if not slug_words:
            return None

        slug = sep.join(slug_words)
        if lowercase:
            slug = slug.lower()
        return slug or None
    except Exception:
        return None