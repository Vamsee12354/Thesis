def validate_form(name,email,number):
    if(name==None or email==None or number==None):
        print("Please fill all the fields and try agian")
        return False
    else:
        if(len(name)>1):
            pass
        else:
            print("Name is invalid")
            return False
        if("@" in email and ".com" in email):
            pass
        else:
            print("Email is invalid")
            return False
        if(len(number)!=10 or not number.isdigit()):
            print("Phone number is invalid")
            return False
        print("Form is valid")
        return True
    
