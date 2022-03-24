# MEE 02/16/22



def open_or_senior(data):
    outputs = [] # make empty list for returning a statement 
    for i in data: # for loop for each  two-part data set
      if i[0] >= 55 and i[1] > 7: # making sure data set fits qualifications
        outputs.append("senior") # info into the output list
      else: # if the dataset doesnt fit qualifications, different info is put into output list
        outputs.append("open") # adding the info 
    return outputs # returning the output list

print(open_or_senior([(59, 12),(55,-1),(12, -2),(12, 12)]) == ['Senior', 'Open', 'Open', 'Open'])
print(open_or_senior([(74, 10),(55, 6),(12, -2),(68, 7)]) == ['Senior', 'Open', 'Open', 'Open'])
print(open_or_senior([(16, 23),(56, 2),(56,  8),(54, 6)]) == ['Open', 'Open', 'Senior', 'Open'])