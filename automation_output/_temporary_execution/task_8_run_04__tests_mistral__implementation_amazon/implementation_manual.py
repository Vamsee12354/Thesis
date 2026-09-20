import unicodedata
import re

def slugify_manual(text, separator=' – ', lowercase=True, ignore=None, truncate=None):
    if not isinstance(text, str) or not isinstance(truncate, (int, type(None))) or (ignore is not None and not isinstance(ignore, (str, list, type(None)))):
        return None
    if not isinstance(separator, str):
        return None
    if ignore is None:
        ignore = []
    if not isinstance(ignore, list):
        ignore = [ignore]
    if not all(isinstance(char, str) for char in ignore):
        return None
    if not isinstance(lowercase, bool):
        return None
    
    def clean_text(text):
        text = unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore').decode('ASCII')
        text = re.sub(r'[^\w\s-]', '', text)
        text = re.sub(r'\s+', separator, text)
        text = re.sub(r'-+', separator, text)
        text = text.strip(separator)
        for char in ignore:
            text = text.replace(char, char.strip(separator))
        return text
    
    slug = clean_text(text)
    if not slug:
        return None
    if lowercase:
        slug = slug.lower()
    if truncate is not None and len(slug) > truncate:
        slug = slug[:truncate]
    return slug
