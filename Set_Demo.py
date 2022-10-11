print("Demonstration of Set")

"""
Data :          Heterogeneous
Ordered :       No         data linit thevalela asto index vise
Indexed :       No            # list like a array
Mutable :       Yes        # data add or remove hoto
Duplicates :    No

"""
# index naste

data = {11,21,51,101,21,11}     # duplicate thevli tari python unique value stoared kartat

data1 = {11, 90.80, True, "Hello"}   # Heterogeneous

print("First set data : ",data)
print("Length of Data :",len(data))

print("Data is Hererogeneous : ", data1)
print("data is Un-ordered : ",data1)
# print("Data at index 2 : ",data[2])     #TypeError: 'set' object is not subscriptable
print("Data with unique elements",data)

# jar data ordered asel tar append function detate
print("Set is inmutable")

# insert element in Set

data.add(211)   # index naste

print("Data after insertion :",data)

# Remove element
data.remove(211)        # data asel tar remove hoto 
print("Data after remove : ",data)

# data.remove(111)  key error : 111     data nesel tar error
# print("Data after remove element ",data)

data.discard(201)   # data asel tar remove and nasel tar error nahi det move forward
print("Data after remove element ",data)