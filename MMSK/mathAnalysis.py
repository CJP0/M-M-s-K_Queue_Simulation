import math

def lambdaN(lam, k, n):
    if n < k:
        return lam
    return 0
    
def muN(mu, s, n):
    if n < s:
        return n*mu
    return s*mu
    
'''    
def PI(lam, mu, s, k, start, end):
    result = 1.0
    for i in range(start, end):
        result *= (lambdaN(lam, k, i) / muN(mu, s, i+1))
    return result

def P0(lam, mu, s, k):
    sum = 0
    for i in range(1, k+1):
        sum += PI(lam, mu, s, k, 0, i)
    return 1 / (1 + sum)
'''

def P0(lam, mu, s, k):
    sum = 1.0
    for i in range(1, s):
        sum += (pow((lam/mu), i) / math.factorial(i))
    sum += ((pow((lam/mu), s) / math.factorial(s)) * ((1-pow((lam/(s*mu)), (k-s+1))) / (1-(lam/(s*mu)))))
    return 1 / sum

def Pn(lam, mu, s, k, n):
    if n < s:
        return ((pow((lam/mu), n)) / math.factorial(n)) * P0(lam, mu, s, k)
    return ((pow((lam/mu), n)) / (math.factorial(s) * pow(s, (n-s)))) * P0(lam, mu, s, k)

def Lq(lam, mu, s, k):
    result = 0
    for i in range(s, (k+1)):
        result += ((i-s) * Pn(lam, mu, s, k, i))
    return result

def L_(lam, mu, s, k):
    sum = 0
    sum2 = 0
    for i in range(0, s):
        temp = Pn(lam, mu, s, k, i)
        sum += i * temp
        sum2 += temp
    sum2 = s * (1 - sum2)
    return (Lq(lam, mu, s, k) + sum + sum2)
    
def lambdaEff(lam, mu, s, k):
    return lam * (1 - Pn(lam, mu, s, k, k))
    
def W_(lam, mu, s, k):
    return (L_(lam, mu, s, k) / lambdaEff(lam, mu, s, k))
    
def Wq(lam, mu, s, k):
    return (Lq(lam, mu, s, k) / lambdaEff(lam, mu, s, k))
    