def CheckEvenX(No):
    return(No % 2 == 0)

Even = lambda No : No % 2 == 0

def main():

    RetX = Even(12)

    if(RetX == True):
        print("Its even")
    else :
        print("Its Odd")

if __name__ == "__main__":
    main()
