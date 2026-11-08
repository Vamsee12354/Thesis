def slugify_manual(text, separator="-", lowercase=True, ignore=None, truncate=None):
    if not isinstance(text, str):
        return None

    if not text:
        return None

    if ignore is None:
        ignore = []
    elif isinstance(ignore, str):
        ignore = [ignore]
    elif not isinstance(ignore, list):
        return None

    if not isinstance(separator, str) or len(separator) != 1:
        return None

    if not isinstance(lowercase, bool):
        return None

    if truncate is not None and (not isinstance(truncate, int) or truncate <= 0):
        return None

    normalized_text = text.strip()
    if not normalized_text:
        return None

    translit_map = {
        '，': ',', '。': '.', '！': '!', '？': '?', '、': ',', '；': ';',
        '：': ':', '（': '(', '）': ')', '【': '[', '】': ']', '「': '[',
        '」': ']', '『': '[', '』': ']', '“': '"', '”': '"', '‘': "'",
        '’': "'", '—': '-', '…': '...', '～': '~', '·': '.', '。': '.',
        '，': ',', '；': ';', '：': ':', '？': '?', '！': '!'
    }

    slug_chars = []
    for char in normalized_text:
        if char in ignore:
            slug_chars.append(char)
            continue

        if char in translit_map:
            char = translit_map[char]

        if char.isalnum():
            slug_chars.append(char)
        elif char.isspace():
            slug_chars.append(separator)
        elif char in {'-', '_'}:
            slug_chars.append(separator)
        else:
            continue

    slug = ''.join(slug_chars)

    if separator:
        slug = separator.join(part for part in slug.split(separator) if part)

    if lowercase:
        slug = slug.lower()

    if truncate is not None and len(slug) > truncate:
        last_sep_index = slug.rfind(separator, 0, truncate)
        if last_sep_index != -1:
            slug = slug[:last_sep_index]
        else:
            slug = slug[:truncate]

    if not slug:
        return None

    return slug