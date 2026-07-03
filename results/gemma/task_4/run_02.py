import math

def get_read_duration(text):
    if not isinstance(text, str):
        return None

    try:
        words = text.split()
        word_count = len(words)

        if word_count == 0:
            return 1

        reading_speed_wpm = 200
        duration = math.ceil(word_count / reading_speed_wpm)

        return max(1, duration)
    except Exception:
        return None