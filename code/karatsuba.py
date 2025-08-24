def karatsuba(u, v, n):
    if(n<=3):
        return u*v
    
    maxMid = n//2
    highU, lowU = divmod(u, 10**maxMid)
    highV, lowV = divmod(v, 10**maxMid)
    highProduct = karatsuba(highU, highV, maxMid)
    lowProduct = karatsuba(lowU, lowV, maxMid)
    crossProduct = karatsuba(highU+lowU, highV+lowV, maxMid+1)
    uv = highProduct*10**(2*maxMid) + (crossProduct - highProduct - lowProduct)*10**maxMid + lowProduct
    return uv

if __name__ == "__main__":
    u = 123456789101112
    v = 1314151617181920
    n = max(len(str(u)), len(str(v)))
    print(karatsuba(u, v, n))