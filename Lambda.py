# Normal Fuctions / Named Functions
# def Functions_Name(Functions_parameters):
#   Function_Body

def Add(No1, No2):
    return No1 + No2


# Lambda Functions / Unnamed functions
# Lambda parameter : body(should be in single line its a limitation of lambda funtions)

AddFunction = lambda A,B : A + B

Ans1 = Add(10,11)
Ans2 = AddFunction(10,11)

print("Addition using normal function : ",Ans1)
print("Addition using Lambda function : ",Ans2)

print("Type of Lambda function is : ",type(AddFunction))