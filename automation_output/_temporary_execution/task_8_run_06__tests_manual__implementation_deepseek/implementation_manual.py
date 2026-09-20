import re
import unicodedata

def slugify_manual(text, separator='-', lowercase=True, ignore=None, truncate=None):
    if not isinstance(text, str):
        return None
    
    if ignore is None:
        ignore = []
    elif isinstance(ignore, str):
        ignore = [ignore]
    
    normalized_text = unicodedata.normalize('NFKD', text)
    slug_parts = []
    current_word = []
    
    for char in normalized_text:
        if char in ignore:
            if current_word:
                slug_parts.append(''.join(current_word))
                current_word = []
            slug_parts.append(char)
        else:
            category = unicodedata.category(char)
            if category.startswith('L') or category.startswith('N'):
                current_word.append(char.lower() if lowercase else char)
            elif category == 'Zs' or category == 'Po' or category == 'Pd' or category == 'Pc':
                if current_word:
                    slug_parts.append(''.join(current_word))
                    current_word = []
    
    if current_word:
        slug_parts.append(''.join(current_word))
    
    slug = []
    for part in slug_parts:
        if part in ignore:
            slug.append(part)
        else:
            cleaned_part = re.sub(r'[^\w\s-]', '', part)
            if cleaned_part:
                slug.append(cleaned_part)
    
    slug = [s for s in slug if s]
    if not slug:
        return None
    
    result = separator.join(slug)
    
    if truncate is not None and truncate > 0:
        parts = result.split(separator)
        truncated = []
        length = 0
        for part in parts:
            if length + len(part) + (1 if truncated else 0) <= truncate:
                truncated.append(part)
                length += len(part) + (1 if truncated else 0)
            else:
                break
        if not truncated:
            return None
        result = separator.join(truncated)
    
    return result
