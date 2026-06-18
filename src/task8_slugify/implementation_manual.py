def slugify_manual(text,separator='-',lowercase=True,ignore=None,truncate=None):
    if len(text)==0:
        return None
    new_text=""
    for i in text:
        if ignore and i in ignore:
            new_text+=i
            continue
        if lowercase:
            i=i.lower()
        if i.isalnum():
            new_text+=i
        elif i==" ":
            if len(new_text)>0 and not new_text.endswith(separator):
                new_text+=separator
    new_text=new_text.strip(separator)
    if truncate is not None:
        parts=new_text.split(separator)
        new_text=""
        for p in parts:
            if len(new_text)==0:
                temp=p
            else:
                temp=new_text+separator+p
            if len(temp)<=truncate:
                new_text=temp
            else:
                break

    return new_text

print(slugify_manual(''))
