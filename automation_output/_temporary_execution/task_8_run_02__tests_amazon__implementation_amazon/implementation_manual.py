import unicodedata
import re

def slugify_manual(text, separator=' – ', lowercase=True, ignore=None, truncate=None):
    if not isinstance(text, str) or not isinstance(truncate, int) or truncate < 0:
        return None
    
    if ignore is None:
        ignore = []
    
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii')
    text = re.sub(r'[^\w\s-]', '', text)
    
    if lowercase:
        text = text.lower()
    
    for char in ignore:
        text = text.replace(char, char.lower() if lowercase else char)
    
    words = text.split()
    if not words:
        return None
    
    slug = separator.join(words)
    if truncate and len(slug) > truncate:
        slug =''.join(words[:truncate//len(slug)]).replace(' ', separator)
    
    slug = re.sub(r'[-\s]+', separator, slug)
    slug = re.sub(r'^' + re.escape(separator) + '|' + re.escape(separator) + '$', '', slug)
    
    if not slug.replace(separator, ''):
        return None
    
    return slug
