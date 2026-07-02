import re
import unicodedata

def slugify_manual(text, separator="-", lowercase=True, ignore=None, truncate=None):
    if not text or isinstance(text, (int, float, bool)):
        return None

    if isinstance(text, str):
        text = unicodedata.normalize("NFKD", text)

    if ignore:
        if isinstance(ignore, str):
            ignore_chars = [ignore]
        else:
            ignore_chars = ignore
        preserved_pattern = re.compile(f"[{''.join(re.escape(char) for char in ignore_chars)}]")
        preserved_chars = preserved_pattern.findall(text)
    else:
        preserved_chars = []

    slug = ""
    for char in text:
        if char in preserved_chars:
            slug += char
            continue

        normalized_char = unicodedata.normalize("NFKD", char)
        decoded_char = normalized_char.encode("ascii", "ignore").decode("ascii")

        if decoded_char.isalnum():
            slug += decoded_char
        elif slug and slug[-1] != separator:
            slug += separator

    slug = re.sub(f"{separator}+", separator, slug)
    slug = slug.strip(separator)

    if lowercase:
        slug = slug.lower()

    if truncate:
        slug_parts = slug.split(separator)
        truncated_slug = []
        current_length = 0

        for part in slug_parts:
            if current_length + len(part) <= truncate:
                truncated_slug.append(part)
                current_length += len(part) + len(separator)
            else:
                break

        slug = separator.join(truncated_slug).strip(separator)

    return slug if slug else None