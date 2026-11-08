import unicodedata
import re

def slugify_manual(text, separator='-', lowercase=True, ignore=None, truncate=None):
    if not isinstance(text, str) or not isinstance(separator, (str, int)):
        return None
    if ignore is None:
        ignore = []
    if not isinstance(ignore, (list, str)):
        return None
    if truncate is not None and not isinstance(truncate, int) or truncate < 0:
        return None
    
    def clean_text(text):
        text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii')
        text = re.sub(r'[^\w\s-]', '', text)
        text = re.sub(r'\s+', separator, text)
        return text
    
    def transliterate(text):
        trans = str.maketrans('ÀÁÂÃÄÅàáâãäåÒÓÔÕÖòóôõöÈÉÊËèéêëÌÍÎÏìíîïÙÚÛÜùúûüÝŸýÿ', 
                          'AAAAAAaaaaaOOOOOooooooEEEEeeeeIIIIiiiiUUUUuuuuYyy')
        return text.translate(trans)
    
    text = clean_text(text)
    text = transliterate(text)
    
    if ignore:
        for char in ignore:
            if isinstance(char, str):
                text = text.replace(char, char)
    
    if lowercase:
        text = text.lower()
    
    if truncate and len(text) > truncate:
        text = text[:truncate]
    
    if not re.search(r'\w', text):
        return None
    
    return text
