import time


def time_decorator(func):
    def wrapper():
        start_time = time.time()
        print(start_time)
        func()
        end_time = time.time()
        print(end_time)

    print(f" Time taken by this function {start_time - end_time}")
    return wrapper()


@time_decorator
def test_ui_1():
    print("Add a function, Time taken by this function")
    time.sleep(5)
