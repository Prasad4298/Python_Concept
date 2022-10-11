"""
Accept One number from users and display factors using while loop
"""

# import Display
# from Display import Display_Factors
# from Display import *

import Display as Dis

def main():

    print("Enter the Number for display its factors")
    iValue = input()

    Dis.Display_Factors(int(iValue))

if __name__ == "__main__":
    main() 