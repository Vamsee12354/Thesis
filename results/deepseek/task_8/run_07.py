import re
import unicodedata

def slugify_manual(text, separator='-', lowercase=True, ignore=None, truncate=None):
    if not text or not isinstance(text, str):
        return None

    if ignore is not None:
        if isinstance(ignore, str):
            ignore = [ignore]
        ignore_pattern = '|'.join(re.escape(char) for char in ignore)

    text = unicodedata.normalize('NFKD', text)
    text = text.encode('ascii', 'ignore').decode('ascii')
    text = re.sub(r'[^\w\s' + (re.escape(separator) if separator else '') + (':' + ignore_pattern if ignore else '') + ']', '', text)

    text = re.sub(r'\s+', separator, text.strip())

    if lowercase:
        text = text.lower()

    if ignore is not None:
        for char in ignore:
            text = text.replace(char, char)

    if truncate is not None and truncate > 0:
        words = text.split(separator)
        truncated_text = []
        current_length = 0
        for word in words:
            if current_length + len(word) + (len(truncated_text) > 0) <= truncate:
                truncated_text.append(word)
                current_length += len(word) + (len(truncated_text) > 1)
            else:
                break
        text = separator.join(truncated_text)

    if not text:
        return None

    return text