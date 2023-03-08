# define the calculator function

def calculator():

    number1 = int(input("Enter first number: ")

    number2 = int(input("Enter second number: "))

    operator = input("Enter operator (+, -, *, /): ")

    

    if operator == '+':

        result = number1 + number2

    elif operator == '-':

        result = number1 - number2

    elif operator == '*':

        result = number1 * number2

    elif operator == '/':

        result = number1 / number2

    else:

        print("Invalid operator")

    print("Result: ", result)
if __name__ == "__main__":

    calculator()
