
num1 = float(input("Please enter your first number "))
num2 = float(input("Thank you! Now please  answer your second number "))
operation = input("What operation are we using ")

if operation == '+':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == '-':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == '*':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == '/':
    result = num1 / num2
    print(f"{num1} / {num2} = {result}")
    
    
