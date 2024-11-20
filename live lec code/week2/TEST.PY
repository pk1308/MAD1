def func1(func):
    def wrapper_func(a, b):
        print("Hey There!")
        if b==0:
            print("Hello!")
            return   
    return  wrapper_func
@func1
def f2(a, b):
    return a%b
S = f2(2,5)

print(S)
