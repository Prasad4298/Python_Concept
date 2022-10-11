"""
Accept input from command line arguments

command :-> python Factors5.py 12

"""

#import sys  (osbased .pyc file)

from Display import *
from sys import *

def main():

    print("Application name is : ",argv[0])  # argv is argument for vectors
    Display_Factors(int(argv[1))

if __name__ == "__main__":
    main() 