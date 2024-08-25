# Create a program , take 2 inputs from the user num1, num2 and give them
# max
# pow num1 to num2
# sub, mul, sum, div.
# Format your out with f{""}

num1 = int(input("Enter the value of num1"))
num2 = int(input("Enter the value of num2"))

print(max(f'{num1, num2}'))
print("Power of two numbers = ", f'{num1 ** num2}')
print("Sum of two numbers =", f'{num1 + num2}')
print("Sub of two numbers =", f'{num1 - num2}')
print("Mul of two numbers =", f'{num1 * num2}')
print("Div of two numbers =", f'{num1 / num2}')
