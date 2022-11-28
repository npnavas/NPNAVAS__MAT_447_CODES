from math import sqrt, ceil
def BSGS(a,b,p):
    a_inv = pow(a,-1,p)
    m = ceil(sqrt(p))

    aj = [(a**j)%p for j in range(0,m)]
    for k in range(0,m):
        if b in aj:
            return f'x = {((k)*m+aj.index(b))%p}'
            break
        else:
            b = (b*(a_inv**m))%p

print(BSGS(5,15,83))
