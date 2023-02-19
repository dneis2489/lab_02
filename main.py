n = 12
sieve = set(range(2, n+1))
while sieve:
    prime = min(sieve)
    print(prime, end = "\t")
    sieve -= set(range(prime, n+1, prime))