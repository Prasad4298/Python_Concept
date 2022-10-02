print("Application to demonstrate Industrial programming")

def Addition(Value1, Value2):        # its a generic function
    Ans = Value1 + Value2
    return Ans

def main():
    print("Enter the first number : ")    
    no1 = int(input())

    print("Enter the second number : ")    
    no2 = int(input())
    
    iRet = Addition(no1,no2)

    print("Addition is : ",iRet)

if __name__  == "__main__":
    main()