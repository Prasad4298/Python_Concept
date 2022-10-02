print("Demonstration of Types of Function Arguments....!")

# Position arguments

def Batches1(name,fees):
    print("Batch name is", name)
    print("Fees are", fees)

print("Demonstration of Position Arguments")

Batches1('python',5000)

Batches1('5000','Angular')
# Keyword Arguments

def Batches2(name, fees):
    print("Batch name is",name)
    print("Fees are",fees)

print("Demonstraion keyword of arguments")

Batches2(fees = 9000, name = 'PPA')
Batches2(name = 'LB',fees = 7500)

# Default arguments

def Batches3 (name, fees = 5000):
    print("batche name is ",name)
    print("fees are", fees)

print("Demonstration of default arguments")
Batches3('Angular',7500)
Batches3('Angular')
Batches3(fees = 9000, name = 'PPA')
Batches3(name = 'LB')

# Variable number of arguments

def Add(*no):
    ans = 0
    for i in no :
        ans = ans + i

    return ans

print("Demonstraion of Variable number os arguments")

ret = Add(10,20,30)
print("Addition is",ret)

ret = Add(10,20,30,40,50,60,70)
print("Addition is",ret)

ret = Add(10,20)
print("Addition is",ret)

# Keyword Variable number of arguments

def StudentInfo(**other):
    print(other)
    for i,j in other.items():
        print(i,j)      # i = key and j = value
        print(i)
        print(j)

print("Demonstration of Keyword Variable number os arguments")

StudentInfo(age = 28, address = "Sinhgad Road", mobile = 9011697535, company = "EasyPay")
