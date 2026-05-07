from slugify import slugify

def slugify_manual(text,seperator='-',lowercase=True,truncate=None,ignore=None):
    if text is None or not text.strip():
        return None
    

    
