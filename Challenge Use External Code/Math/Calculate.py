
import  math
def SumTwo(One,Two) :
    return (One + Two)

def ArithmeticOperations(Number1, Number2, OperationType):
    if OperationType == "+":
        print(Number1 + Number2)
    elif OperationType == "-":
        print(Number1 - Number2)
    elif OperationType == "*":
        print(Number1 * Number2)
    elif OperationType == "/":
        print(Number1 / Number2)
    elif OperationType == "%":
        print(Number1 % Number2)
    elif OperationType == "power":
        print(math.pow(Number1, Number2))
    elif OperationType == "sar" :
        print(math.sqrt(Number1))
    else :
        print("We don't support this operation")