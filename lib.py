def clear(n,k):
    print("the num in binary after clear ",bin(n & ~(1 << (k))))
    return (n & ~(1 << (k)))
def toggle(n,k):
    print("the num in binary after toggle ",bin(n ^ (1 << ( k) )))
    return(n ^ (1 << ( k) ))

def sett(n,k):
    print("the num in binary after set ",bin(n | (1 << (k))))
    return (n | (1 << (k)))
def gett(n,k):
    return(n & (1<<(k)))
