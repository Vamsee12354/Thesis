import re
import unicodedata

def slugify_manual(text, separator="-", lowercase=True, ignore=None, truncate=None):
    if not isinstance(text, str) or not text.strip():
        return None

    if ignore is None:
        ignore = []

    normalized_text = unicodedata.normalize('NFKD', text)
    ascii_text = normalized_text.encode('ascii', 'ignore').decode('ascii')

    pattern = r'[^\w\s{}]'.format(re.escape(''.join(ignore)))
    cleaned_text = re.sub(pattern, '', ascii_text)

    words = re.split(r'\s+', cleaned_text.strip())
    filtered_words = [word for word in words if word]

    if not filtered_words:
        return None

    slug = separator.join(filtered_words)

    if lowercase:
        slug = slug.lower()

    if truncate is not None and truncate > 0:
        if len(slug) <= truncate:
            return slug
        truncated_slug = slug[:truncate]
        last_separator_index = truncated_slug.rfind(separator)
        if last_separator_index != -1:
            truncated_slug = truncated_slug[:last_separator_index]
        slug = truncated_slug if truncated_slug else None

    return slug if slug else None