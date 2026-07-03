import re
import unicodedata

def slugify_manual(text, separator='-', lowercase=True, ignore=None, truncate=None):
    if not text or not isinstance(text, str):
        return None
    if ignore is None:
        ignore = []
    if isinstance(ignore, str):
        ignore = [ignore]
    ignore_pattern = '|'.join(re.escape(char) for char in ignore)
    text = unicodedata.normalize('NFKD', text)
    cleaned_text = ''.join(c for c in text if unicodedata.category(c) != 'Mn')
    pattern = r'[^\w\s{}]'.format(re.escape(ignore_pattern)) if ignore_pattern else r'[^\w\s]'
    cleaned_text = re.sub(pattern, '', cleaned_text)
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
    cleaned_text = cleaned_text.replace(' ', separator)
    if lowercase:
        cleaned_text = cleaned_text.lower()
    if truncate:
        cleaned_text = cleaned_text[:truncate]
        last_sep_index = cleaned_text.rfind(separator)
        if last_sep_index != -1:
            cleaned_text = cleaned_text[:last_sep_index]
    if not cleaned_text:
        return None
    return cleaned_text