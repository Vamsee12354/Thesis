import math
def get_read_duration(text):
    if len(text.split())>0:
        time=math.ceil(len(text.split())/200)
    else:
        time=1
    return time
