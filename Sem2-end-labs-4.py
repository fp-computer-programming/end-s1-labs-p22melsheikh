# MEE 02/16/22



def validate_pin(pin):
    if(type(pin) != str or len(pin) not in [4, 6]): # check that pin fits length qualifications of 4 or 6 characters and is string
        return(False) # if not, then function returns False
    for value in pin: # for loop so each character is checked
       if value not in "0123456789": # since it is a string, this is how I checked to make sure all the characters were numbers, and also positive
            return(False) # returning False if not a positive number
    return(True) # If the pin makes it through all the statements, it must be a valid pin, so return True

print(validate_pin("1234567") == False)
print(validate_pin("apple") == False)
print(validate_pin("1") == False)
print(validate_pin("1234") == True)