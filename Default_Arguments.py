def Area(Radius, PI):
    Result = PI * Radius * Radius
    return Result

def Area2(Radius, PI = 3.14):       # default arguments
    Result = PI * Radius * Radius
    return Result

def Area3(Radius, PI = 3.14):       # default arguments + default
    Result = PI * Radius * Radius
    return Result

def Area4(Radius, PI = 3.14):       # default arguments + default
    Result = PI * Radius * Radius
    return Result

def main():
    RValue = 10.5
    PIVAlue = 3.14

    Ans = Area(RValue,PIVAlue)      # Positional arguments
    print("Area of Circle is : ",Ans)

    Ans = Area(PI = PIVAlue, Radius = PIVAlue)  # key word arguments
    print("Area of Circle is : ",Ans)

    Ans = Area2(RValue)     # Positional arguments 2nd is default
    print("Area of Circle is : ",Ans)

    Ans = Area3(Radius = RValue)       # key word paramets and 2nd is default
    print("Area of Circle is : ",Ans)

    Ans = Area4(Radius = RValue, PI = 7.10)       # key word paramets
    print("Area of Circle is : ",Ans)

if __name__ == "__main__":
    main()