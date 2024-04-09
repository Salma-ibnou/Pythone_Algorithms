def f(x,y):
    global a
    a = 45
    x,y=y,x
    b = 17
    print(a,b,x,y)
a,b,x,y = 3,15,3,4
f(9,81)
print(a,b,x,y) 