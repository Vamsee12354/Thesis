from unicodedata import normalize, category
import re

def slugify_manual(text, separator='-', lowercase=True, ignore=None, truncate=None):
    if not isinstance(text, str):
        return None

    if not text:
        return None

    if ignore is None:
        ignore = []
    elif isinstance(ignore, str):
        ignore = [ignore]

    try:
        normalized_text = normalize('NFKD', text)
    except Exception:
        return None

    slug_parts = []
    current_part = []
    in_word = False

    for char in normalized_text:
        if char in ignore:
            if current_part:
                slug_parts.append(''.join(current_part))
                current_part = []
            slug_parts.append(char)
            in_word = False
            continue

        if category(char).startswith('L') or category(char).startswith('N'):
            current_part.append(char)
            in_word = True
        else:
            if in_word:
                slug_parts.append(''.join(current_part))
                current_part = []
                in_word = False

    if current_part:
        slug_parts.append(''.join(current_part))

    if not slug_parts:
        return None

    processed_parts = []
    for part in slug_parts:
        if part in ignore:
            processed_parts.append(part)
        else:
            cleaned_part = re.sub(r'[^\w\s-]', '', part)
            cleaned_part = re.sub(r'[\s]+', ' ', cleaned_part)
            if cleaned_part:
                processed_parts.append(cleaned_part)

    if not processed_parts:
        return None

    slug = ' '.join(processed_parts)
    slug = re.sub(r'[\s]+', separator, slug)

    if lowercase:
        slug = slug.lower()

    if truncate is not None:
        if not isinstance(truncate, int) or truncate <= 0:
            return None
        words = slug.split(separator)
        truncated_words = []
        current_length = 0
        for word in words:
            if current_length + len(word) <= truncate:
                truncated_words.append(word)
                current_length += len(word) + len(separator)
            else:
                break
        slug = separator.join(truncated_words)
        if not slug:
            return None

    return slug