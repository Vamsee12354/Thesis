import unicodedata
import re

def slugify_manual(text, separator=' – ', lowercase=True, ignore=None, truncate=None):
    if not isinstance(text, str) or not isinstance(separator, str) or not isinstance(lowercase, bool) or (ignore is not None and not (isinstance(ignore, str) or isinstance(ignore, list))):
        return None
    
    if ignore is None:
        ignore = []
    if not isinstance(ignore, list):
        ignore = [ignore]
    
    if not text.strip():
        return None
    
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii')
    text = re.sub(r'[^\w\s-]', '', text)
    
    for char in ignore:
        text = text.replace(char, char)
    
    text = re.sub(r'\s+', separator, text)
    
    if lowercase:
        text = text.lower()
    
    if truncate and len(text) > truncate:
        text = text[:truncate]
    
    if not re.search(r'\w', text):
        return None
    
    return text
