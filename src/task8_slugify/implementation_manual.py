def slugify_manual(text,seperator='-',lowercase=True,ignore=None,truncate=None):
    if len(text)==0:
        return None
    new_text=""
    for i in text:
        if ignore and i in ignore:
            continue
        if lowercase:
            i=i.lower()
        if i.isalnum():
            new_text+=i
        elif i==" ":
            if len(new_text)>0 and not new_text.endswith(seperator):
                new_text+=seperator
    new_text=new_text.strip(seperator)
    if truncate is not None:
        new_text=new_text[:truncate]    
    new_text=new_text.strip(seperator)

    return new_text

print(slugify_manual(''))
