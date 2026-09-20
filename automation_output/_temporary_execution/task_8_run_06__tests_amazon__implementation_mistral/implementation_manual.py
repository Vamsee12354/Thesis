from unicodedata import normalize
from typing import Optional, Union

def slugify_manual(
    text: str,
    separator: str = "-",
    lowercase: bool = True,
    ignore: Optional[Union[str, list[str]]] = None,
    truncate: Optional[int] = None,
) -> Optional[str]:
    if not isinstance(text, str):
        return None

    if not text:
        return None

    if ignore is not None:
        if isinstance(ignore, str):
            ignore = [ignore]
        ignore_set = set(ignore)
    else:
        ignore_set = set()

    normalized_text = normalize("NFKD", text)

    slug_parts = []
    current_part = []

    for char in normalized_text:
        if char in ignore_set:
            if current_part:
                slug_parts.append("".join(current_part))
                current_part = []
            slug_parts.append(char)
        elif char.isalnum():
            current_part.append(char)
        else:
            if current_part:
                slug_parts.append("".join(current_part))
                current_part = []

    if current_part:
        slug_parts.append("".join(current_part))

    if not slug_parts:
        return None

    filtered_parts = []
    for part in slug_parts:
        if part.isalnum():
            filtered_parts.append(part)
        elif part in ignore_set:
            filtered_parts.append(part)

    if not filtered_parts:
        return None

    slug = separator.join(filtered_parts)

    if lowercase:
        slug = slug.lower()

    if truncate is not None:
        if truncate <= 0:
            return None
        if len(slug) > truncate:
            slug = slug[:truncate]

    return slug