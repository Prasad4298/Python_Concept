values = [10,20,30,40,50]

print(values[0])        # Starting pt (0)
print(values[1])
print(values[2])        # displacement (1)
print(values[3])
print(values[4])        # ending pt ((len(values)-1)

# for i in range(start, end, displacement):

for i in range(0,len(values),1):
    print(i)
    print("values is :-> ",values[i])

print("Removing displacement")

for i in range(0,len(values)):
    print(i)
    print("values is :-> ",values[i])

for no in values:
    print(no)       # no madhe values 10,20,30,40,50