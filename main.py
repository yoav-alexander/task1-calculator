
def divide(num1, num2):  # divides num1 by num2
    if not num2:
        print("divide by zero")
        return
    return num1 / num2


def multiply(num1, num2):  # multiples num1 by num2
    return num1 * num2


def add(num1, num2):
    return num1 + num2


def power(base, exponent):
    return base ** exponent


def sub(num1, num2):
    if num1 == num2 == 0:
        print("Invalid operation ")
        return
    return num1 - num2


def main():
    num1, num2 = input("enter two numbers:\n"), input()
    if not num1.isnumeric() or not num2.isnumeric():
        print("invalid Input")
        main()
        return

    num1, num2 = int(num1), int(num2)
    print("enter a number corresponding to the operation you want:")
    operator = input(" 1. add \n 2. subtract \n 3.multiply \n 4.divide \n 5. power\n")
    if not operator.isnumeric() or 0 >= int(operator) >= 5:
        print("invalid operator")
        main()
        return

    operator = int(operator)
    if operator == 1:
        result = add(num1, num2)
    elif operator == 2:
        result = sub(num1, num2)
    elif operator == 3:
        result = multiply(num1, num2)
    elif operator == 4:
        result = divide(num1, num2)
    else:
        result = power(num1, num2)
    print(f"the result is: {result}")


if __name__ == '__main__':
    main()
