def IsValidPassword(password):
    errors=[]
    if len(password)==0:
        return "Please fill the password"
    if len(password)<12 or len(password)>72:
        errors.append("Length must be between 12 and 72 characters")
    lowerCase=False
    upperCase=False
    num=False
    special=False
    for char in password:
        if(char.isdigit()):
            num=True
        if(char.islower()):
            lowerCase=True
        if(char.isupper()):
            upperCase=True
        if(not char.isalnum() or not char.isspace()):
            special=True
            
    if not lowerCase:
        errors.append("Password must contain a lowercase letter")
    if not upperCase:
        errors.append("Password must contain an uppercase letter")
    if not special or not num:
        errors.append("Password must contain a special character or a number")
    if len(errors)==0:
        return "The password is valid"
    else:
        return errors

print(IsValidPassword("abcdefg"))