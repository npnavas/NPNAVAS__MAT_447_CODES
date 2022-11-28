from sympy.ntheory import factorint #import to get prime factors
from sympy.ntheory.factor_ import totient #import to get phi
def isPrimRoot(a,n):
    '''
    PARAMETERS
    ----------
    a: num you want to check
    n: modulus of your system

    RETRUNS
    -------
    Bool value
    '''
    phi = totient(n) #get phi(n)
    qj = list(factorint(phi).keys()) #generate list of prime factors with no powers
    dj = [] #initializer for values of dj

    for j in range(len(qj)):
        dj.append(int((phi)/(qj[j]))) #populates dj

    out = [(a**(dj[p]))%n for p in range(len(dj))] #make list of a^dj

    ##CHECK TO SEE IF a IS PRIM ROOT OF n##
    if 1 in out: #isn't prim root
        return False
    elif 1 not in out: #is prim root
        return True

print(isPrimRoot(7, 601))
