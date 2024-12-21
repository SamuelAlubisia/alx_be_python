num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number"))
operation = input("Choose the operation (+, -, *, /):")
match operation:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
           if num2 == 0:
            result = "Cannot divide by 0"
           else:
            result = num1 / num2
    case _:
        result = "Invalid operation"
print(f"The result is {result}.")