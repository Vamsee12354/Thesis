import math
def get_read_duration(text: str) -> int:
    if not isinstance(text, str):
        return None

    try:
        words = text.split()
        word_count = len(words)

        if word_count == 0:
            return 1

        reading_speed_wpm = 200
        estimated_minutes = word_count / reading_speed_wpm

        return math.ceil(estimated_minutes) if estimated_minutes > 0 else 1
    except Exception:
        return None