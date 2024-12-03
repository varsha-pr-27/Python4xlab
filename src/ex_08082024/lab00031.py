def outer_function():
    variable1 = 23


def inner_function1():
    print(variable1)


def inner_function2():
    print(variable1)


inner_function1()
inner_function2()

outer_function()


