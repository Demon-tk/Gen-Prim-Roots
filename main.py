import sympy
from math import gcd


def get_input():
    return input("Enter your number: ")


def power(x, pow, n):
    return sympy.Pow(x, pow) % n


def calculate_first_prim_root(n):
    # Check if number is prime
    if not sympy.isprime(n):
        print("{} is not a prime number, and cannot be a generator".format(n))
        return None
    # Get phi
    phi = n - 1
    # Get prime factors
    prime_factors = sympy.primefactors(phi)
    # Calculate powers
    for x in range(2, n):
        check = any(power(x, phi // p_factor, n) == 1 for p_factor in prime_factors)
        if not check:
            return x
    return None


def calculate_other_prim_root(n, first_prime_root):
    my_set = {first_prime_root}
    for x in range(2, n-1):
        if gcd(x, n - 1) == 1:
            my_set.add(str(first_prime_root) + '^' + str(x % n))
    return my_set


if __name__ == '__main__':
    # Get number
    n = 97#int(get_input())
    # Do calculations
    first_prime_root = calculate_first_prim_root(n)
    if first_prime_root is not None:
        prime_generators = calculate_other_prim_root(n, first_prime_root)
        print(prime_generators)
        print(len(prime_generators))
