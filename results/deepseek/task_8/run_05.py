import re
import unicodedata

def slugify_manual(text, separator='-', lowercase=True, ignore=None, truncate=None):
    if not text:
        return None
    
    if ignore is None:
        ignore = []
    
    text = unicodedata.normalize('NFKD', text)
    text = text.encode('ascii', 'ignore').decode('ascii')
    
    cleaned_text = []
    for char in text:
        if char in ignore:
            cleaned_text.append(char)
        elif char.isalnum():
            cleaned_text.append(char)
        elif char.isspace():
            cleaned_text.append(separator)
    
    slug = ''.join(cleaned_text)
    slug = re.sub(f'[{re.escape(separator)}]+', separator, slug)
    slug = slug.strip(separator)
    
    if lowercase:
        slug = slug.lower()
    
    if truncate is not None and truncate > 0:
        words = slug.split(separator)
        truncated_slug = []
        length = 0
        for word in words:
            if length + len(word) + len(separator) <= truncate:
                truncated_slug.append(word)
                length += len(word) + len(separator)
            else:
                break
        slug = separator.join(truncated_slug)
    
    if not slug:
        return None
    
    return slug


