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
            ascii_chars = ''.join(c for c in decomp if unicodedata.category(c).startswith('L') or c.isdigit())
            return ascii_chars

        text = ''.join(transliterate(c) for c in text)
        if lowercase:
            text = text.lower()

        pattern = f'[^{re.escape(separator)}a-z0-9{"".join(re.escape(c) for c in ignore_set)}]+'
        text = re.sub(pattern, separator, text)
        text = re.sub(f'{re.escape(separator)}+', separator, text)
        text = text.strip(separator)

        if not text:
            return None

        if truncate is not None and truncate > 0:
            if len(text) <= truncate:
                return text
            parts = text.split(separator)
            truncated_parts = []
            length = 0
            for part in parts:
                part_len = len(part)
                if truncated_parts:
                    part_len += len(separator)
                if length + part_len > truncate:
                    break
                truncated_parts.append(part)
                length += part_len
            text = separator.join(truncated_parts)
            if not text:
                return None

        return text
    except Exception:
        return None