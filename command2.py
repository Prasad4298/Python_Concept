"""
Command :-> python command2.py 11 10
output :-> 21

"""

from sys impor t*

def Addition(A,B):
    Ans = 0
    Ans = A + B
    return Ans
    
def main():
    
    if(len(argv) != 3)
        print("Invalid number of argument")
        exit()
    
    iRet = Addition(int(argv[1]), int(argv[2]))
    print("Addition is :-> ",iRet)
    
if __name__ == "__main__":
    main() 
    
 