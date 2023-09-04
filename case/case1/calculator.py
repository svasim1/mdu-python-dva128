import math

operators = {'add': '+', 'sub': '-', 'mul': '*', 'div': '/',}

def add(a,b):
    return f"RESULT: {a} + {b} = {a+b}";
def sub(a,b):
    return a - b;
def mul(a,b):
    return a * b;
def div(a,b):
    return a / b;

def selector(mType, a, b):
    if mType == "add":
        return add(a, b)
    elif mType == "sub":
        return sub(a, b)
    elif mType == "mul":
        return mul(a, b)
    elif mType == "div":
        return div(a, b)

close = False
while not close:
    print('******************************************' + '\n' + '   Mathlete Calculator' + '\n' + '------------------------------------------' + "\n" + "add | Add two numbers" + "\n" + "sub | Subtract two number" + "\n" + "mul | Multiply two numbers" + "\n" + "div | Divide two numbers" + "\n" + '------------------------------------------')
    mathType = input('Selection > ')
    if mathType == "add" or mathType == "sub" or mathType == "mul" or mathType == "div":
        print('------------------------------------------' + "\n" + "Calculating 'c' for expression:" + "\n\n" + "a " + operators[mathType] + " b = c" + "\n\n" + "Please, enter values for 'a' and 'b'." + "\n")
        try:
            primary = float(input('a = '))
            secondary = float(input('b = '))
            if secondary == 0 and mathType == 'div':
                print('Undefined')
                input("Press ENTER to continue... ")
                continue
        except ValueError:
            print("Please enter a valid number")
            input("Press ENTER to continue... ")
            continue
        print(selector(mathType, primary, secondary))
        input("Press ENTER to continue... ")
        continue
    elif mathType == "exit":
        close = True
    else:
        print("Please enter a valid mode")
        input("Press ENTER to continue... ")
        continue

   