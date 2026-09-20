
import unicodedata
def slugify_manual(text,separator='-',lowercase=True,ignore=None,truncate=None):
    if text is None or text=="":
        return None
    text=text.strip()
    if text=="":
        return None
    if not ignore :
        ignore=[]

    decomposed=unicodedata.normalize('NFKD',text)
    text="".join(ch for ch in decomposed if not unicodedata.combining(ch))

    new_text=""
    if lowercase:
        text=text.lower()
    for i in text:
        if i.isalnum() or  i in ignore:
            new_text+=i
        else:
                    if not new_text.endswith(separator):
                        new_text+=separator
    if truncate:
        truncated_text=[]
        result=""
        truncated_text=new_text.split(separator)
        for j in truncated_text:
            if result=="":
                result=j
            elif len(result+separator+j)<truncate and not result.endswith(separator) and result:
                result=result+separator+j
        new_text=result
    new_text=new_text.strip(separator)
    if new_text.strip(separator)=="":
        return None
    return new_text

print(slugify_manual("café Bjorn!"))