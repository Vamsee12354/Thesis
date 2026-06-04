def IsValidPassword(password):
    if(len(password) > 5 and len(password) < 15):
        lowerCase = False
        upperCase = False
        num = False
        special = False
        for char in password:
            if(char.isdigit()):
                num = True
            if(char.islower()):
                lowerCase = True
            if(char.isupper()):
                upperCase = True
            if(not char.isalnum()):
                special = True
        result= lowerCase and upperCase and num and special
        if result:
            print("The password is valid")
            return True
        else:
            print("Follow the password rules accordingly")
            return False

    else:
        print("Follow the password length and rules accordingly")
        return False



print(IsValidPassword(""))