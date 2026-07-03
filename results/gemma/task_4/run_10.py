import math

def get_read_duration(text):
    if not isinstance(text, str):
        return None

    try:
        words = text.split()
        word_count = len(words)

        if word_count == 0:
            return 1

        words_per_minute = 200
        duration = math.ceil(word_count / words_per_minute)

        return max(1, duration)
    except Exception:
        return None