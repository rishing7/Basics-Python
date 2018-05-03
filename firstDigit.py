t = int(input())
while t>0 :
    i = 0
    num_array = []
    n = int(input())
    while i<n:
        num_array.append(int(input()))
        i = i+1
    res = 1
    for j in num_array:
        res = res*j
    while(res>=10):
        res = res/10
    print(res)
    t = t-1
