"""Unit tests for schwifty.py. Run with `py.test schwifty.py -v`"""

import schwifty


def test_fibonnaci():
    fibs10 = schwifty.fibonaccis(10)
    assert list(fibs10) == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]


def test_is_prime():
    fibs30 = schwifty.fibonaccis(30)
    assert ([n for n in fibs30 if schwifty.is_prime(n)] ==
            [2, 3, 5, 13, 89, 233, 1597, 28657, 514229])


def test_prime_large():
    fibs = (n for n in schwifty.fibonaccis(30) if n >= 5)
    assert ([n for n in fibs if schwifty._is_large_prime(n)] ==
            [13, 21, 89, 233, 1597, 28657, 514229])


def test_fizzbuzzes():
    """compares `fizzbuzzes` generator to known good output"""
    fizzbuzzes = schwifty.fizzbuzzes(20)
    assert list(map(str, fizzbuzzes)) == SAMPLE_OUTPUT


# desired output of `python3.6 schwifty.py 20`
SAMPLE_OUTPUT = """
1
1
BuzzFizz
Buzz
Fizz
8
BuzzFizz
Buzz
34
Fizz
BuzzFizz
Buzz
BuzzFizz
377
Fizz
Buzz
BuzzFizz
2584
4181
FizzBuzz
""".strip().split()

