import re
import unicodedata

def slugify_manual(text, separator='-', lowercase=True, ignore=None, truncate=None):
    if not isinstance(text, str) or not text.strip():
        return None
    
    if ignore is None:
        ignore = []
    elif isinstance(ignore, str):
        ignore = [ignore]
    
    preserved_chars = set()
    for char in ignore:
        if char in text:
            preserved_chars.add(char)
    
    normalized = unicodedata.normalize('NFKD', text)
    slug = []
    for char in normalized:
        if char in preserved_chars:
            slug.append(char)
            continue
        if unicodedata.category(char)[0] == 'L':
            slug.append(char)
        elif unicodedata.category(char)[0] == 'N':
            slug.append(char)
        elif char.isspace():
            slug.append(' ')
        else:
            continue
    
    slug = ''.join(slug)
    slug = re.sub(r'[^\w\s' + re.escape(''.join(preserved_chars)) + ']', '', slug)
    slug = re.sub(r'\s+', ' ', slug).strip()
    
    if not slug:
        return None
    
    if lowercase:
        slug = slug.lower()
    
    slug_parts = slug.split(' ')
    final_slug = []
    for part in slug_parts:
        if part:
            final_slug.append(part)
    
    slug = separator.join(final_slug)
    
    if truncate is not None and truncate > 0:
        if len(slug) > truncate:
            truncated = slug[:truncate]
            if separator:
                last_sep = truncated.rfind(separator)
                if last_sep != -1:
                    truncated = truncated[:last_sep]
            slug = truncated
    
    if not slug:
        return None
    
    return slug
 