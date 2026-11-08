import re
def validate_form(first_name,last_name,email,subject,message,privacy):
        error_msg=[]
        if first_name is not None and len(first_name.strip())>0:
            pass
        else:
            error_msg.append("Please Type First Name")
        if last_name is not None and len(last_name.strip())>0:
            pass
        else:
            error_msg.append( "Please Type Last Name" )
        if email is None or len(email.strip())==0:
            error_msg.append("Please Type EmailID")
        elif re.match(r'^[^\s@]+@[^\s@]+\.[^\s@]+$',email.strip()):
            pass
        else:
            error_msg.append ("Email standards not followed")
        if subject is not None and len(subject.strip())>0:
            pass
        else:
            error_msg.append("Please Type Subject")

        if message is not None and len(message.strip())>0:
            pass
        else:
            error_msg.append("Please Type Message")
        if(privacy==True):
            pass
        else:
            error_msg.append ("Please confirm the privacy policy")        
        if len(error_msg)==0:
            return (f"Form is valid. Details:{first_name},{last_name},{email},{subject},{message},{privacy}")
        else:
            return error_msg
        
    
print(validate_form("Axxs","James","abc@gmail.com","Question","Hallo!",True))