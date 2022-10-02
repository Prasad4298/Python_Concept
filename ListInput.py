# Accept the element from users and add into List.

def main():
    Arr = list()    # by using this we can create emty list in python
          # list class cha object create kala

    print("Enter how many elements you want to store?")
    size = int(input())

    print("Please Enter the values.......!")

    for i in range(0,size,1):
        no = int(input())
        Arr.append(no)      # Arr.insrt(i,no)

    print(Arr)

if __name__ == "__main__":
    main()