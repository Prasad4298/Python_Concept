"""
Accept One number from users and display factors
"""

def Display_Factors(iNo):

    for i in range(1,int(iNo/2)+1,1):
        if iNo % i == 0:
            print(i)

def main():

    print("Enter the Number for display its factors")
    iValue = input()

    Display_Factors(int(iValue))

if __name__ == "__main__":
    main()