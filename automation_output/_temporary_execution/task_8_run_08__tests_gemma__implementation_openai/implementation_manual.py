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
                decomp = unicodedata.normalize('NFKD', char)
                return ''.join(c for c in decomp if unicodedata.category(c) != 'Mn')
            if char.isalnum():
                return char
            return ''

        text = ''.join(transliterate(c) for c in text)
        text = text.lower() if lowercase else text

        for ch in ignore:
            text = text.replace(ch, f' {ch} ')

        text = re.sub(r'[^\w\s' + re.escape(''.join(ignore)) + ']', '', text, flags=re.UNICODE)
        text = re.sub(r'\s+', ' ', text).strip()

        words = []
        for word in text.split():
            if all(c in ignore_set for c in word):
                words.append(word)
            else:
                cleaned_word = ''.join(c for c in word if c.isalnum() or c in ignore_set)
                if cleaned_word:
                    words.append(cleaned_word)

        if not words:
            return None

        slug = separator.join(words)

        if truncate is not None and isinstance(truncate, int) and truncate > 0:
            if len(slug) <= truncate:
                return slug
            truncated_words = []
            length = 0
            for w in words:
                w_len = len(w)
                sep_len = len(separator) if truncated_words else 0
                if length + sep_len + w_len > truncate:
                    break
                if truncated_words:
                    truncated_words.append(separator)
                    length += sep_len
                truncated_words.append(w)
                length += w_len
            slug = ''.join(truncated_words)
            if not slug:
                return None

        return slug if slug else None
    except Exception:
        return None