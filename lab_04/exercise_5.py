def all_factors(n: int) -> list:
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors

def prime(n: int) -> bool:
    if all_factors(n) != [1, n]:
        return False
    return True

def prime_factors(n: int) -> list:
    factors = all_factors(n)
    prime_factors = []
    for factor in factors:
        if prime(factor):
            prime_factors.append(factor)
    return prime_factors

def smaller_primes(n: int) -> list:
    primes = []
    for i in range(2, n):
        if prime(i):
            primes.append(i)
    return primes

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    factors = all_factors(n)
    print(', '.join(str(factor) for factor in factors))
    if prime(n):
        print(f"{n} is a prime number.")
    else:
        print(f"{n} is not a prime number.")
        print("Prime factors: " + ', '.join(str(factor) for factor in prime_factors(n)))
    print("Smaller prime numbers: " + ', '.join(str(prime) for prime in smaller_primes(n)))