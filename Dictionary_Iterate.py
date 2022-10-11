print("Demonstration of Dictionay")

"""
Data :              Heterogeneous
Ordered :           Yes         
Indexed :           No            
Mutable :           Yes     # add or remove elements        
Duplicates(key) :   No
Duplicates(value) : Yes 

"""

#           key    value
Batches = {"PPA" : 18000, "LB" : 16700, "Python" : 16500, "Angular" : 15000}

print("Data of Dictonary Batches : ",Batches)

print("Data travelsal using for loop")

for x in Batches:
    print(x)

print("_________________________________________________________")

print("Data travelsal using for loop with key and value")

for x in Batches:
    print(x,Batches[x])

print("_________________________________________________________")

print("Data travelsal using for loop using get method")

for x in Batches:
    print(x,Batches.get(x))     # its like a [] bracket

print("_________________________________________________________")

keyBatches = Batches.keys()     # method used for get keys

print(type(keyBatches))
print(keyBatches)

valueBatches = Batches.values()
print(type(valueBatches))
print(valueBatches)

for i in range(0,len(Batches),1):
    print("Batch name is : ",keyBatches[i], end = "")
    print("Fees are : ",valueBatches[i])