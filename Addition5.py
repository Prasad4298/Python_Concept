print("Application to demonstrate Industrial programming")

def main():
    print("Enter the first number : ")    
    no1 = input()
    print(type(no1))

    print("Enter the second number : ")    
    no2 = input()
    print(type(no2))
    
    Ans = int(no1) + int(no2)

    print("Addition is : ",Ans)

if __name__  == "__main__":
    main()