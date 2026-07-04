import re
import unicodedata

def slugify_manual(text, separator='-', lowercase=True, ignore=None, truncate=None):
    if not text:
        return None
    
    if ignore is None:
        ignore = []
    
    normalized_text = unicodedata.normalize('NFKD', text)
    cleaned_text = []
    
    for char in normalized_text:
        if char in ignore:
            cleaned_text.append(char)
        elif char.isalnum():
            cleaned_text.append(char)
        elif char.isspace():
            cleaned_text.append(' ')
        else:
            cleaned_text.append('')
    
    cleaned_text = ''.join(cleaned_text)
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
    
    if lowercase:
        cleaned_text = cleaned_text.lower()
    
    slug = re.sub(r'\s+', separator, cleaned_text)
    
    if truncate is not None and truncate > 0:
        words = slug.split(separator)
        truncated_slug = []
        length = 0
        for word in words:
            if length + len(word) + len(truncated_slug) > truncate:
                break
            truncated_slug.append(word)
            length += len(word)
        slug = separator.join(truncated_slug)
    
    if not slug:
        return None
    
    return slug


