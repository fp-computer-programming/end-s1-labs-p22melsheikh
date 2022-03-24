# MEE 02/16/22


def filter_list(l):
    list1 =[] # Empty list 
    for x in l: # For loop 
        if type(x) != str: # Filter 
            list1.append(x) # Add integers and floats 
    return list1 # Return the new list 
print(filter_list([1,2,'a','b']) == [1,2])
print(filter_list([1,'a','b',0,15]) == [1,0,15])
print(filter_list([1,2,'aasf','1','123',123]) == [1,2,123])