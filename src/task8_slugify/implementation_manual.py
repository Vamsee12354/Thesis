from slugify import slugify

def slugify_manual(text,seperator='-',lowercase=True,truncate=None,ignore=None):
    new_text=""
    for i in text:
        if lowercase:
            i=i.lower()
        if i.isalnum():
            new_text+=i
        elif i==" ":
            new_text+='-'
       
    new_text=new_text.strip(seperator)
    return new_text

 
    

    
