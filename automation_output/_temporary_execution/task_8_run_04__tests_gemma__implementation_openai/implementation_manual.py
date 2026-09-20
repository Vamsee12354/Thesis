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
        sep_escaped = re.escape(sep)

        pattern_ignore = '|'.join(re.escape(i) for i in ignore_set) if ignore_set else None

        def preserve_ignore(m):
            return m.group(0).replace(' ', '\0')

        if ignore_set:
            text = re.sub('|'.join(re.escape(i) for i in ignore_set), preserve_ignore, text)

        text = text.lower() if lowercase else text

        text = re.sub(r'\s+', sep, text)
        text = re.sub(r'[^a-z0-9' + sep_escaped + ''.join(re.escape(i) for i in ignore_set) + ']+', '', text)
        text = re.sub(sep_escaped + '{2,}', sep, text)
        text = text.strip(sep)

        if ignore_set:
            text = text.replace('\0', ' ')

        if truncate is not None and isinstance(truncate, int) and truncate > 0:
            if len(text) <= truncate:
                return text if text else None
            parts = text.split(sep)
            truncated_parts = []
            length = 0
            for part in parts:
                part_len = len(part)
                if truncated_parts:
                    if length + 1 + part_len > truncate:
                        break
                    length += 1 + part_len
                else:
                    if part_len > truncate:
                        break
                    length += part_len
                truncated_parts.append(part)
            text = sep.join(truncated_parts)
            if not text:
                return None

        return text if text else None
    except Exception:
        return None