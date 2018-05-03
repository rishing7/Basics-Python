from functools import partial
def add(a,b,c,d):
    return 1000*a+100*b+10*c+d
d = partial(add,1,2,3))
print(d(5))
