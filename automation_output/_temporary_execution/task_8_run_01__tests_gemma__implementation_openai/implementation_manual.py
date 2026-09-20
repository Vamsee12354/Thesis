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
            decomp = unicodedata.normalize('NFKD', char)
            ascii_equiv = ''.join(c for c in decomp if unicodedata.category(c).startswith('L') or c.isdigit())
            return ascii_equiv

        text = ''.join(transliterate(c) for c in text)
        text = text.strip()
        if not text:
            return None

        pattern_ignore = '|'.join(re.escape(i) for i in ignore_set) if ignore_set else None

        def preserve_ignore(m):
            return m.group(0).replace(' ', '\0')

        if pattern_ignore:
            text = re.sub(pattern_ignore, preserve_ignore, text)

        text = text.lower() if lowercase else text
        text = re.sub(r'[^\w\s' + re.escape(''.join(ignore_set)) + ']', '', text)
        text = text.replace('\0', ' ')
        text = re.sub(r'\s+', ' ', text).strip()
        if not text:
            return None

        words = text.split()
        if not words:
            return None

        if truncate is not None and truncate > 0:
            truncated_words = []
            length = 0
            for word in words:
                add_len = len(word) + (len(separator) if truncated_words else 0)
                if length + add_len > truncate:
                    break
                truncated_words.append(word)
                length += add_len
            words = truncated_words
            if not words:
                return None

        slug = separator.join(words)
        if not slug:
            return None
        return slug
    except Exception:
        return None