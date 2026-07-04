import re
import unicodedata

def slugify_manual(text, separator='-', lowercase=True, ignore=None, truncate=None):
    if not isinstance(text, str) or not text.strip():
        return None
    
    if ignore is None:
        ignore = []
    elif isinstance(ignore, str):
        ignore = [ignore]
    
    normalized = unicodedata.normalize('NFKD', text)
    allowed_chars = set()
    
    for c in normalized:
        if ord(c) < 128 and c.isalnum() or c in ignore:
            allowed_chars.add(c)
    
    cleaned = []
    word = []
    
    for c in normalized:
        if c in allowed_chars:
            if c.isalnum():
                word.append(c.lower() if lowercase else c)
            else:
                if word:
                    cleaned.append(''.join(word))
                    word = []
                cleaned.append(c)
        else:
            if word:
                cleaned.append(''.join(word))
                word = []
    
    if word:
        cleaned.append(''.join(word))
    
    slug_parts = []
    for item in cleaned:
        if item not in ignore:
            if item.isalnum():
                slug_parts.append(item)
        else:
            slug_parts.append(item)
    
    slug = separator.join(slug_parts)
    slug = re.sub(rf'{re.escape(separator)}+', separator, slug)
    slug = slug.strip(separator)
    
    if truncate is not None and truncate > 0:
        parts = slug.split(separator)
        truncated = []
        length = 0
        
        for part in parts:
            if length + len(part) + (1 if truncated else 0) <= truncate:
                truncated.append(part)
                length += len(part) + (1 if truncated else 0)
            else:
                break
        
        slug = separator.join(truncated)
        slug = slug[:truncate].rstrip(separator)
    
    if not slug:
        return None
    
    return slug
