print("Application to demonstrate Industrial programming")

import AdditionModule

def main():
    print("Value of __name__ from main is : ",__name__)
    print("Enter the first number : ")    
    no1 = int(input())

    print("Enter the second number : ")    
    no2 = int(input())
    
    iRet = AdditionModule.Addition(no1,no2)

    print("Addition is : ",iRet)

if __name__  == "__main__":
    main().