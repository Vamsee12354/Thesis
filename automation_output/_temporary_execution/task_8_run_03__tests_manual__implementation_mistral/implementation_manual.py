def slugify_manual(text, separator="-", lowercase=True, ignore=None, truncate=None):
    if not isinstance(text, str) or not text:
        return None

    if ignore is None:
        ignore = []
    elif isinstance(ignore, str):
        ignore = [ignore]

    if not isinstance(separator, str) or len(separator) != 1:
        return None

    if not isinstance(lowercase, bool):
        return None

    if truncate is not None and (not isinstance(truncate, int) or truncate <= 0):
        return None

    translit_map = {
        '，': ',', '。': '.', '！': '!', '？': '?', '、': ',', '；': ';',
        '：': ':', '（': '(', '）': ')', '【': '[', '】': ']', '「': '[',
        '」': ']', '『': '[', '』': ']', '《': '<', '》': '>', '…': '...',
        '—': '-', '～': '~', '‘': "'", '’': "'", '“': '"', '”': '"',
        '　': ' ', ' ': ' ', '¡': 'i', '¿': '?', '¢': 'c', '£': 'l',
        '¥': 'y', '€': 'e', '©': 'c', '®': 'r', '°': 'o', '±': '+',
        'µ': 'u', '§': 's', '÷': '/', '×': 'x', '¶': 'p', '†': 't',
        '‡': 't', '•': '-', '…': '...', '′': "'", '″': '"', '‾': '-',
        '‒': '-', '–': '-', '—': '-', '‘': "'", '’': "'", '“': '"',
        '”': '"', '„': '"', '«': '"', '»': '"', '‹': '"', '›': '"',
        '‚': "'", '„': '"', '“': '"', '”': '"', '‘': "'", '’': "'",
        '′': "'", '″': '"', '‵': "'", '‶': '"', 'ʻ': "'", 'ʼ': "'",
        'ʽ': "'", 'ʾ': "'", 'ʿ': "'", 'ˀ': "'", 'ˁ': "'", '˂': '<',
        '˃': '>', '˄': '^', '˅': 'v', 'ˆ': '^', 'ˇ': 'v', 'ˈ': "'",
        'ˉ': '-', 'ˊ': "'", 'ˋ': '`', 'ˌ': ',', 'ˍ': '_', 'ˎ': "'",
        'ˏ': "'", 'ː': ':', 'ˑ': ':', '˒': "'", '˓': "'", '˔': "'",
        '˕': "'", '˖': '+', '˗': '-', '˘': 'u', '˙': '.', '˚': 'o',
        '˛': 'a', '˜': '~', '˝': '"', '˞': "'", '˟': 'x', 'ˠ': 'g',
        'ˡ': 'l', 'ˢ': 's', 'ˣ': 'x', 'ˤ': "'", '˩': 'v', '˪': 'v',
        '˫': 'v', 'ˬ': 'v', '˭': '|', 'ˮ': 'r', '˯': 'v', '˰': 'v',
        '˱': '(', '˲': ')', '˳': 'o', '˴': "'", '˵': "'", '˶': '"',
        '˷': 'v', '˸': ':', '˹': "'", '˺': "'", '˻': '[', '˼': ']',
        '˽': '|', '˾': ']', '˿': '|'
    }

    normalized_text = []
    for char in text:
        if char in ignore:
            normalized_text.append(char)
        else:
            normalized_text.append(translit_map.get(char, char))

    normalized_text = ''.join(normalized_text)

    slug_parts = []
    current_part = []
    for char in normalized_text:
        if char.isalnum():
            current_part.append(char)
        else:
            if current_part:
                slug_parts.append(''.join(current_part))
                current_part = []
            if char.isspace():
                continue
            if char != separator:
                slug_parts.append(separator)

    if current_part:
        slug_parts.append(''.join(current_part))

    slug = ''.join(slug_parts)

    if not slug:
        return None

    if lowercase:
        slug = slug.lower()

    if truncate is not None:
        if separator:
            parts = slug.split(separator)
            truncated_parts = []
            total_length = 0
            for part in parts:
                if total_length + len(part) + (1 if truncated_parts else 0) <= truncate:
                    truncated_parts.append(part)
                    total_length += len(part) + (1 if truncated_parts else 0)
                else:
                    break
            slug = separator.join(truncated_parts)
        else:
            slug = slug[:truncate]

    if not slug:
        return None

    return slug