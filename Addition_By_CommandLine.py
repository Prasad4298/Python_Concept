"""
Command :-> python command1.py 11 Hello 11.5

"""

from sys impor t*

def Addtion(iNo1,iNo2):

    return iNo1 + iNo2

def main():
    
    print("Total number of arguments are : "len(argv))
    
    if((argv[1] != 0) || (argv[2] != 0)):
        print("please Enter input while compiling the code")
        return 
    
    iRet = Addtion(argv[1],argv[2])
    print("Addtion is : ",iRet);
    
if __name__ == "__main__":
    main() 
    
 