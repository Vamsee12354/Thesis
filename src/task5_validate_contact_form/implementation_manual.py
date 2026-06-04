def validate_form(name,email,subject,message,privacy):
    if(name==None or email==None or subject==None or message==None or privacy==None or name=="" or email=="" or subject=="" or message==""):
        return "Please fill all the fields and try again"
        
    else:
        if(len(name)>1):
            pass
        else:
            return "Name is invalid"
        if("@" in email and ".com" in email):
            pass
        else:
            return "Email is invalid"
        if(len(subject)>1):
            pass
        else:
            return "Please Type Subject"
        if(len(message)>1):
            pass
        else:
            return ("Please Type Message")
            

        if(privacy==True):
            pass
        else:
            return ("Please confirm the privacy policy")        
    
        return (f"Form is valid. Details are :{name,email,subject,message,privacy} ")
        
    
