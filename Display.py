"""
Accept One number from users and display factors using while loop
"""

def Display_Factors(iNo):

    i = 1
    while (i <= int(iNo/2)):
        if ((iNo % i) == 0):
            print(i)
        i = i + 1

def main():

    print("Enter the Number for display its factors")
    iValue = input()

    Display_Factors(int(iValue))

if __name__ == "__main__":
    main() 