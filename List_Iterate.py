print("Demonstration of List eteration")

"""
Data : Heterogeneous
Ordered :       Yes         data linit thevalela asto index vise
Indexed :       Yes
Mutable :       Yes
Duplicates :    Yes

"""

Data = [11,21,51,101]

print("Output using for Loop......!")

for no in Data:
    print(no,end = " ")
print()


print("Output using for with index")

for i in range(0,len(Data),1):
    print(Data[i], end = " ")
print()


print("Output using while Loop ")

i = 0
while(i < len(Data)):
    print(Data[i], end = " ")
    i = i + 1
print()