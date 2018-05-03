def sum(*args):
    a, b = args
    return a+b
a = int(input("Enter first Number: "))
b = int(input("Enter first Number: "))
t = sum(a,b)
print("Sum of %r and %r is %r"%(a,b,t))
