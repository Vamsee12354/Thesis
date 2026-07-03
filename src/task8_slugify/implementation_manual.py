
import unicodedata
def slugify_manual(text,separator='-',lowercase=True,ignore=None,truncate=None):
    if text is None:
        return None
    text=text.strip()
    if text=="":
        return None
    result=""
    chinese_characters={
        "你": "ni",
        "好": "hao",
        "世": "shi",
        "界": "jie"
    }
    for i in text:
        if ignore and i in ignore:
            result+=i
            continue
        elif  i.isspace():
            if separator!='' and not result.endswith(separator) and result:
                result+=separator
        elif i in (chinese_characters):
                chinese_text=chinese_characters[i]
                if lowercase:
                    chinese_text=chinese_text.lower()
                if separator!='' and not result.endswith(separator) and result:
                    result+=separator
                result+=chinese_text
                if separator!='':
                    result+=separator
        elif i.isalnum():
            if lowercase:
                i=i.lower()
            result+=i
        else:
             ascii_text=unicodedata.normalize('NFKD',i).encode('ascii','ignore').decode('ascii')
             if ascii_text:
                if lowercase:
                    ascii_text=ascii_text.lower()
                result+=ascii_text

    result=result.strip(separator)
    if result=='':
        return None
    if truncate is not None:
            if separator=='':
                result=result[:truncate]
            else:
                split_text=result.split(separator)
                truncate_result=""  
                for i in split_text:
                    if truncate_result=='':
                        temp=i
                    else:
                        temp=truncate_result+separator+i
                    if len(temp)<=truncate:
                        truncate_result=temp
                    else:
                        break
                result=truncate_result
            if result=='': 
                return None            
    return result
            





 
