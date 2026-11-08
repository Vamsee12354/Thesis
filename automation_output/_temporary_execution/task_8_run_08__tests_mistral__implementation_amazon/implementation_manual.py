import unicodedata
import re

def slugify_manual(text, separator='-', lowercase=True, ignore=None, truncate=None):
    if not isinstance(text, str) or not isinstance(separator, (str, int)):
        return None
    if ignore is None:
        ignore = []
    if isinstance(ignore, str):
        ignore = [ignore]
    if not all(isinstance(c, str) for c in ignore):
        return None
    if truncate is not None and not isinstance(truncate, int) or truncate < 0:
        return None

    def clean_text(text):
        text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii')
        text = re.sub(r'[^\w\s-]', '', text)
        text = re.sub(r'[-\s]+', separator, text)
        text = re.sub(r'^[-\s]+', '', text)
        text = re.sub(r'[-\s]+$', '', text)
        return text

    def transliterate(text):
        trans = str.maketrans('ÀÁÂÃÄÅàáâãäåǺǻÇçÐđÈÉÊËèéêëĘęĞğĠġĢģĤĥĦħÌÍÎÏìíîïİıĴĵĶķĸŁłÑñŃńŅņŇňØøÒÓÔÕÖØòóôõöŐőŔŕŘřŚśŤťŢţŦŧÙÚÛÜùúûüŲųŴŵÝýŶŷŸÿŻżŹźŽž', 'AAAAAAaaaaaaCcDdEEEEEeeeeeEeeeIiIJjKkLlNnNnnNnOOOOOOOOOooooooRrRrSsSsSsTtTtTtUUUUUUUUUuuuuuuuUuYyYyYZzZzZz', 'Œœ')
        return text.translate(trans)

    text = clean_text(text)
    if not text:
        return None

    for char in ignore:
        text = text.replace(char, char)

    if lowercase:
        text = text.lower()

    if truncate is not None:
        words = text.split(separator)
        if len(''.join(words)) > truncate:
            words = words[:truncate//len(separator)]
            text = separator.join(words)

    return text
