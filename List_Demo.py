print("Demonstration of List")

"""
Data : Heterogeneous
Ordered :       Yes         data linit thevalela asto index vise
Indexed :       Yes            # list like a array
Mutable :       Yes
Duplicates :    Yes

"""
data = [11,21,51,101,21,11]     # duplicatae value stoared 

data1 = [11, 90.80, True, "Hello"]   # Heterogeneous

print("Data is Hererogeneous : ", data1)
print("data is ordered : ",data1)
print("Data at index 2 : ",data[2])
print("DAta with duplicate elements",data)

# jar data ordered asel tar append function detate
print("List is mutable")
data.append(201)    # append kelyavar data end la add hoto
print("DAta after Append : ",data)
data.remove(51)
data.pop()      # pop kela tar end cha data delete hoto

print("DAta after pop : ",data)
