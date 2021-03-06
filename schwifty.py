"""
From the Swift Nav coding challenge:

In the programming language of your choice,
write a program generating the first n Fibonacci numbers F(n), printing

"Buzz" when F(n) is divisible by 3.
"Fizz" when F(n) is divisible by 5.
"FizzBuzz" when F(n) is divisible by 15.
"BuzzFizz" when F(n) is prime.
the value F(n) otherwise.

We encourage you to compose your code for this question in a way that
represents the quality of code you produce in the workplace - e.g.
tests, documentation, linting, dependency management
(though there's no need to go this far).
"""

from __future__ import print_function
import argparse


def fizzbuzzes(n):
    """For a maximum of `n` fibonnaci numbers,
    print 'Fizz', 'Buzz', 'FizzBuzz', 'BuzzFizz' or the number based
    on the FizzBuzz spec"""
    for fib in fibonaccis(n):
        if not fib % 15:
            yield "FizzBuzz"
        elif not fib % 5:
            yield "Fizz"
        elif not fib % 3:
            yield "Buzz"
        elif is_prime(fib):
            yield "BuzzFizz"
        else:
            yield fib


def fibonaccis(n):
    """Generates the fibonacci sequence for `n` iterations"""
    val_a, val_b = 1, 1
    yield val_a
    yield val_b
    for _ in range(n - 2):
        val_a, val_b = val_b, val_a + val_b
        yield val_b


# known early Fibonacci primes
# from http://mathworld.wolfram.com/FibonacciPrime.html
EARLY_FIB_PRIMES = {2, 3, 5, 13, 89, 233, 1597, 28657, 514229}
MAX_KNOWN_PRIME = max(EARLY_FIB_PRIMES)


def is_prime(num):
    """Returns True if `num` is prime, False otherwise.
    Checks for membership in our eary known primes before running
    the inefficient primality test."""
    return (num in EARLY_FIB_PRIMES or
            (num > MAX_KNOWN_PRIME and
             _is_large_prime(num)))


def _is_large_prime(num):
    """Inefficient primality test, but we can get away with this simple
    implementation because we don't expect users to be running
    print_fizzbuzz(n) for Fib(n) > 514229"""
    if not num % 2 or not num % 5:
        return False
    test = 5
    while test*test <= num:
        if not num % test or not num % (test+2):
            return False
        test += 6
    return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("num_iterations", type=int)
    args = parser.parse_args()
    for fizzbuzz in fizzbuzzes(args.num_iterations):
        print(fizzbuzz)

