# Continue statement along with program to print odd numbers

for number in range(10):  # 1, 2, 3, 4, 5, 6, 7, 8, 9
    if number % 2 == 0:
        continue  # 1, 3, 5, 7, 9
    else:
        print(number)
