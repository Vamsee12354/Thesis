import math

def get_read_duration(text):
    if not isinstance(text, str):
        return 1
    
    words = text.split()
    word_count = len(words)
    
    if word_count == 0:
        return 1
    
    minutes = math.ceil(word_count / 200)
    return max(1, minutes)