# used to find all prime numbers.
# Precompute all the prime numbers.
# O(root(n))

def find_primes(n):
    prime = [True] *(n+1) # 0..20
    p = 2
    while p*p <= n:
        if prime[p]:
            for i in range(p*2, n+1, p):
                prime[i] = False
        p+=1
    
    prime[0]=prime[1] = False

    for i in range(n+1):
        if prime[i]:
            print(i)

find_primes(20)