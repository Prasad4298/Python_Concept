# List in python (just like a array in behind the curtains)
values = [10,20,30,40]

print(values)

print(type(values))     # List

print(len(values))      # return no of element only applicable for list

print(values[0])
print(values[1])
print(values[2])
print(values[3])

# values[4] = 50        he chalat nahi

values.append(50)   # append function as it applicable in java collection
print(values)

values.insert(2,11)    # insert function accept the 2 parameter 1st is index no. and 2nd is data
print("Data after insert ")
print(values)

values.insert(15,51)        # insert data at index 15
print("size of list is now :  ",len(values))
print("data after insert at position 15 ")
print(values)

values.remove(20)
print(values)

values.append(50) # append is use to insert data at last position 
print(values)   # List support the duplicate values

print(type(values[0]))      # type of 0 element is Int
                            # and type of values is List

values.append(90.89)    # support the heteroginity
print(values)

# insert data in specific index

