def my_decorator(func):
    def wrapper():
        print("Before the function is called")
        func()
        print("After the function is called")
        print("Secure driving")

    return wrapper()


@my_decorator
def driver_bike():
    print("I am driving")
