# MEE 02/16/22


def get_middle(s):
    middle = len(s) // 2 # half the string
    if len(s) % 2 == 0: # if string has even number of characters, the middle is technically two characters
        return s[(middle - 1): (middle + 1)] # returning the two middle characters
    else: # if string isnt an even number of characters, it only has one middle character
        return s[middle] # returning the middle character


print(get_middle("test") == "es")
print(get_middle("testing") == "t")
print(get_middle("of") == "of")