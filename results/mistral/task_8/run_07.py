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

    translit_map = {
        '，': ',', '。': '.', '！': '!', '？': '?', '、': ',', '；': ';', '：': ':',
        '（': '(', '）': ')', '【': '[', '】': ']', '「': '[', '」': ']', '『': '[', '』': ']',
        '‘': "'", '’': "'", '“': '"', '”': '"', '—': '-', '…': '...', '～': '~',
        'á': 'a', 'à': 'a', 'â': 'a', 'ä': 'a', 'ã': 'a', 'å': 'a',
        'é': 'e', 'è': 'e', 'ê': 'e', 'ë': 'e',
        'í': 'i', 'ì': 'i', 'î': 'i', 'ï': 'i',
        'ó': 'o', 'ò': 'o', 'ô': 'o', 'ö': 'o', 'õ': 'o', 'ø': 'o',
        'ú': 'u', 'ù': 'u', 'û': 'u', 'ü': 'u',
        'ý': 'y', 'ÿ': 'y',
        'ç': 'c',
        'ñ': 'n',
        'š': 's', 'š': 's',
        'ž': 'z', 'ž': 'z',
        'č': 'c', 'č': 'c',
        'ć': 'c',
        'đ': 'd',
        'ł': 'l',
        'ž': 'z',
        'ß': 'ss',
        'α': 'a', 'β': 'b', 'γ': 'g', 'δ': 'd', 'ε': 'e', 'ζ': 'z', 'η': 'i',
        'θ': 'th', 'ι': 'i', 'κ': 'k', 'λ': 'l', 'μ': 'm', 'ν': 'n', 'ξ': 'x',
        'ο': 'o', 'π': 'p', 'ρ': 'r', 'σ': 's', 'ς': 's', 'τ': 't', 'υ': 'y',
        'φ': 'f', 'χ': 'ch', 'ψ': 'ps', 'ω': 'o',
        'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E',
        'Ж': 'Zh', 'З': 'Z', 'И': 'I', 'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M',
        'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U',
        'Ф': 'F', 'Х': 'Kh', 'Ц': 'Ts', 'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Shch',
        'Ъ': '', 'Ы': 'Y', 'Ь': '', 'Э': 'E', 'Ю': 'Yu', 'Я': 'Ya',
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e',
        'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'i', 'к': 'k', 'л': 'l', 'м': 'm',
        'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
        'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch',
        'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya',
        '你': 'ni', '好': 'hao', '世': 'shi', '界': 'jie'
    }

    slug_parts = []
    current_part = []
    in_word = False

    for char in text:
        lower_char = char.lower()

        if char in ignore:
            if in_word:
                slug_parts.append(''.join(current_part))
                current_part = []
                in_word = False
            slug_parts.append(char)
            continue

        if char.isalnum():
            current_part.append(lower_char if lowercase else char)
            in_word = True
        else:
            if char.isspace():
                if in_word:
                    slug_parts.append(''.join(current_part))
                    current_part = []
                    in_word = False
            else:
                translit_char = translit_map.get(char, '')
                if translit_char:
                    if in_word:
                        slug_parts.append(''.join(current_part))
                        current_part = []
                        in_word = False
                    if translit_char != '-':
                        current_part.append(translit_char)
                        in_word = True
                else:
                    if in_word:
                        slug_parts.append(''.join(current_part))
                        current_part = []
                        in_word = False

    if in_word:
        slug_parts.append(''.join(current_part))

    if not slug_parts:
        return None

    slug = separator.join(slug_parts)

    if truncate is not None:
        if len(slug) <= truncate:
            pass
        else:
            last_sep_index = slug.rfind(separator, 0, truncate)
            if last_sep_index != -1:
                slug = slug[:last_sep_index]
            else:
                slug = slug[:truncate]

    if not slug:
        return None

    return slug