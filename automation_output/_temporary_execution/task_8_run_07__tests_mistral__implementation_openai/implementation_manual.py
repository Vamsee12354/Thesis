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
            ascii_chars = ''.join(c for c in decomp if unicodedata.category(c).startswith('L') or c.isdigit())
            return ascii_chars

        text = ''.join(transliterate(c) for c in text)
        if not text:
            return None

        sep = separator if isinstance(separator, str) else chr(separator)
        text = text.replace(' ', sep)
        pattern = f'[^{re.escape(sep)}\\w{"".join(re.escape(c) for c in ignore_set)}]+'
        text = re.sub(pattern, sep, text)
        text = re.sub(f'{re.escape(sep)}+', sep, text)
        text = text.strip(sep)
        if lowercase:
            text = text.lower()
        if not text:
            return None
        if truncate is not None and isinstance(truncate, int) and truncate > 0:
            if len(text) <= truncate:
                return text
            parts = text.split(sep)
            truncated_parts = []
            length = 0
            for part in parts:
                part_len = len(part)
                if truncated_parts:
                    part_len += len(sep)
                if length + part_len > truncate:
                    break
                truncated_parts.append(part)
                length += part_len
            text = sep.join(truncated_parts)
            if not text:
                return None
        return text
    except Exception:
        return None