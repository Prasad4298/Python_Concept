"""
Command :-> python command2.py 11 10
output :-> 21

"""

# import sys is important when using command line argument

from sys import *

def Addition(A,B):
    Ans = 0
    Ans = A + B
    return Ans
    
def main():
    
    print("Welcome to : ",argv[0])
    
    if(len(argv) == 2):
        if((argv[1] == "--U") || (argv[1] == "--u")):
            print("Use the application as : ")
            print("python Name_of_Application First_number Second_Number)
            
        if((argv[1] == "--H") || (argv[1] == "--H")):
            print("Help : This application is used to perform additon of 2 numbers")
            exit()
            
    if(len(argv) != 3):
        print("Invalid Number of arguments")
        print("please use --u flag to get the usage")
        exit()
    
    iRet = Addition(int(argv[1]), int(argv[2]))
    print("Addition is :-> ",iRet)
    
    print("Thank you for using the application ")
    print("Marvellous Infosystems by Piyush Manohar Khairnar")
    
if __name__ == "__main__":
    main() 
    
 # jar import sys as lehil tar prattek argv chya aadhi sys.argv as lihala pahije
 
 # length of argv is minimum 1 becouse its argv[0] is file name is 1st argument