# Convert values into int from string

def decor(func):
    def wrapper(x,y):
        if isinstance(x, str):
            x = int(x)
        elif isinstance(y, str):
            y = int(y)
        func(x,y)
    return wrapper



@decor
def devision_1(x,y):
    print(x/y)

devision_1(4, "4")