# N number of arguments
def Add(*Values):
    print("Type of Values is : ",type(Values))
    print("Number of arguments are : ",len(Values))

    Sum = 0
    
    for no in Values:
        Sum = Sum + no

    return Sum


def main():
    Ans = Add(10,20,30,40,50)
    print("Addition is : ",Ans)

if __name__ == "__main__":
    main()