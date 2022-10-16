def CheckEven(iNo):
    if(iNo % 2 == 0):
        return True
    else :
        return False

def CheckEvenX(No):
    return(No % 2 == 0)

def main():

    Ret = CheckEven(12)

    if(Ret == True):
        print("Its even")
    else :
        print("Its Odd")

    
    RetX = CheckEvenX(12)

    if(RetX == True):
        print("Its even")
    else :
        print("Its Odd")

if __name__ == "__main__":
    main()