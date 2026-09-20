import re
import unicodedata


def slugify_manual(
    text,
    separator="-",
    lowercase=True,
    ignore=None,
    truncate=None
):
    if not isinstance(text, str):
        return None

    if ignore is None:
        ignore = []

    normalized_text = unicodedata.normalize('NFKD', text)
    cleaned_text = []
    current_word = []
    ignore_chars = ignore if isinstance(ignore, list) else list(ignore)

    for char in normalized_text:
        if char in ignore_chars:
            if current_word:
                cleaned_word = ''.join(current_word)
                cleaned_text.append(cleaned_word)
                current_word = []
            cleaned_text.append(char)
        else:
            category = unicodedata.category(char)
            if category.startswith('L') or category.startswith('N'):
                current_word.append(char.lower() if lowercase else char)
            elif char.isspace() or category.startswith('Z'):
                if current_word:
                    cleaned_word = ''.join(current_word)
                    cleaned_text.append(cleaned_word)
                    current_word = []
            else:
                pass

    if current_word:
        cleaned_word = ''.join(current_word)
        cleaned_text.append(cleaned_word)

    slug_parts = []
    for item in cleaned_text:
        if item in ignore_chars:
            slug_parts.append(item)
        else:
            cleaned_item = re.sub(r'[^\w\s-]', '', item, flags=re.UNICODE)
            if cleaned_item:
                slug_parts.append(cleaned_item)

    slug = separator.join(slug_parts)

    while '  ' in slug:
        slug = slug.replace('  ', ' ')
    slug = slug.strip()

    if truncate is not None and truncate > 0:
        if len(slug) > truncate:
            slug = slug[:truncate]
            while slug and not slug[-1].isalnum() and slug[-1] not in ignore_chars:
                slug = slug[:-1]

    if not slug:
        return None

    return slug
 