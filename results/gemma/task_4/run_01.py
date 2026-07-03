
import math

def get_read_duration(text):
    if not isinstance(text, str):
        return None
    
    words = text.split()
    word_count = len(words)
    
    if word_count == 0:
        return 1
        
    reading_speed = 200
    minutes = math.ceil(word_count / reading_speed)
    
    return max(1, minutes)