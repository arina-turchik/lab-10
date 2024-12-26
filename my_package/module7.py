def intersect(Z,X):
    C=[]
    for z in Z:
        for x in X:
            if z==x:
                C.append(z)
                break
    return C

def sqr_3(n):
    if n==0:
        return 0
    else:
        return (3+sqr_3(n-1))**(0.5)