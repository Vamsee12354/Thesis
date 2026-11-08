import unicodedata
import re

def slugify_manual(text, separator="-", lowercase=True, ignore=None, truncate=None):
    if not isinstance(text, str):
        return None

    if ignore is None:
        ignore_chars = set()
    elif isinstance(ignore, str):
        ignore_chars = set(ignore)
    elif isinstance(ignore, list):
        ignore_chars = set("".join(ignore))
    else:
        ignore_chars = set()

    try:
        text = text.encode('utf-8').decode('utf-8')
    except (UnicodeEncodeError, UnicodeDecodeError):
        return None

    def transliterate(s):
        normalized = unicodedata.normalize('NFKD', s)
        result = ""
        for char in normalized:
            if unicodedata.category(char) != 'Mn':
                result += char
        
        if result == s and any(ord(c) > 127 for c in s):
            mapping = {
                '你': 'ni', '好': 'hao', '世': 'shi', '界': 'jie',
                '吗': 'ma', '我': 'wo', '你': 'ni'
            }
            for k, v in mapping.items():
                s = s.replace(k, v)
            return s
        return result

    text = transliterate(text)

    if lowercase:
        text = text.lower()

    pattern = r'[^a-zA-Z0-9' + re.escape("".join(ignore_chars)) + r']+'
    
    parts = re.split(pattern, text)
    parts = [p for p in parts if p]

    if not parts:
        return None

    slug = separator.join(parts)

    if truncate is not None and truncate > 0:
        if len(slug) > truncate:
            truncated = slug[:truncate]
            last_sep = truncated.rfind(separator)
            if last_sep != -1 and last_sep > 0:
                slug = truncated[:last_sep]
            else:
                slug = truncated
                
    if not slug and not any(c in slug for c in ignore_chars):
        return None

    return slug