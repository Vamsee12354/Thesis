import re
import unicodedata

def slugify_manual(text, separator='-', lowercase=True, ignore=None, truncate=None):
    if not text:
        return None
    
    if ignore is None:
        ignore = []
    elif isinstance(ignore, str):
        ignore = [ignore]
    
    normalized = unicodedata.normalize('NFKD', text)
    ascii_letters = []
    
    for char in normalized:
        if char in ignore:
            ascii_letters.append(char)
            continue
        
        category = unicodedata.category(char)
        if category == 'Zs':
            ascii_letters.append(' ')
        elif category.startswith('L') or category.startswith('N'):
            ascii_letters.append(char.lower() if lowercase else char)
    
    slug = ''.join(ascii_letters)
    slug = re.sub(r'[^\w\s' + re.escape(''.join(ignore)) + ']', '', slug)
    slug = re.sub(r'\s+', ' ', slug).strip()
    
    if not slug:
        return None
    
    slug = slug.replace(' ', separator)
    
    while separator * 2 in slug:
        slug = slug.replace(separator * 2, separator)
    
    if truncate is not None and truncate > 0:
        parts = slug.split(separator)
        truncated = []
        total_length = 0
        
        for part in parts:
            if total_length + len(part) + (1 if truncated else 0) <= truncate:
                truncated.append(part)
                total_length += len(part) + (1 if truncated else 0)
            else:
                break
        
        if not truncated:
            last_part = parts[0][:truncate]
            if last_part:
                slug = last_part
            else:
                return None
        else:
            slug = separator.join(truncated)
    
    if lowercase:
        slug = slug.lower()
    
    return slug if slug else None
