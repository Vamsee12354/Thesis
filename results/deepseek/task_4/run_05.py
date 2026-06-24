import math

def get_read_duration(text):
    if not text.strip():
        return 1
    words = text.split()
    word_count = len(words)
    minutes = math.ceil(word_count / 200)
    return max(minutes, 1)