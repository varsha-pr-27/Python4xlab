num1 = int(input("Enter the value of num1"))  # 10
num2 = int(input("Enter the value of num2"))  # 11
num3 = int(input("Enter the value of num3"))  # 8

if num1 > num2 and num1 > num3:
    print("Max is = ", f'{num1}')
elif num2 > num1 and num2 > num3:
    print("Max is = ", f'{num2}')
else:
    print("Max is ", f'{num3}')
