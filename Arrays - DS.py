def reverseArray(a):
    x = 0
    y = len(a)-1
    
    while x<y:

        a[x], a[y] = a[y], a[x]
        x = x+1
        y = y-1
    return a