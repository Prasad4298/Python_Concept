# Accept the two number from user and return the Maximum number.

print("Application is user to Return largest number")

def Maximum(iNo1,iNo2):     # positional parameters
    if iNo1 > iNo2:
        return iNo1
    else:
        return iNo2
        
def main():
    print("Enter the 1St Number");
    iNo1 = int(input())

    print("Enter the 2nd Number");
    iNo2 = int(input())

    iRet = Maximum(iNo1, iNo2)

    print("Maximum Number is : ",iRet)

if __name__  == "__main__":
    main()