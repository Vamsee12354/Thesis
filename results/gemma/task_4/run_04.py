import math

def get_read_duration(text: str) -> int:
    if not isinstance(text, str):
        return None

    try:
        words = text.split()
        word_count = len(words)

        if word_count == 0:
            return 1

        minutes = word_count / 200
        return max(1, math.ceil(minutes))
    except Exception:
        return None