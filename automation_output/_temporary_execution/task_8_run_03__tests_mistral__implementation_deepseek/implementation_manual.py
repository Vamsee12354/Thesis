import unicodedata
import re

def slugify_manual(text, separator='-', lowercase=True, ignore=None, truncate=None):
    if not text:
        return None
    
    if ignore is None:
        ignore = []
    
    normalized_text = unicodedata.normalize('NFKD', text)
    ascii_text = normalized_text.encode('ascii', 'ignore').decode('unicode-escape')
    
    slug_parts = []
    current_word = []
    
    for char in ascii_text:
        lower_char = char.lower()
        if char in ignore:
            if current_word:
                slug_parts.append(''.join(current_word))
                current_word = []
            slug_parts.append(char)
        elif char.isalnum():
            current_word.append(lower_char if lowercase else char)
        else:
            if current_word:
                slug_parts.append(''.join(current_word))
                current_word = []
    
    if current_word:
        slug_parts.append(''.join(current_word))
    
    slug = separator.join([part for part in slug_parts if part])
    
    if not slug:
        return None
    
    if truncate is not None:
        parts = slug.split(separator)
        truncated_slug = []
        current_length = 0
        for part in parts:
            if current_length + len(part) + (1 if truncated_slug else 0) <= truncate:
                truncated_slug.append(part)
                current_length += len(part) + (1 if truncated_slug else 0)
            else:
                break
        if not truncated_slug:
            return None
        slug = separator.join(truncated_slug)[:truncate]
    
    return slug if slug else None
