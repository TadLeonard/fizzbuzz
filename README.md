# FizzBuzz: a short coding challenge for Swift Navigation

The challenge:
```
In the programming language of your choice,
write a program generating the first n Fibonacci numbers F(n), printing
"Buzz" when F(n) is divisible by 3.
"Fizz" when F(n) is divisible by 5.
"FizzBuzz" when F(n) is divisible by 15.
"BuzzFizz" when F(n) is prime.
the value F(n) otherwise.
```

## Usage

From the command line: `swift_challenge.py [-h] num_iterations`. Sample output:

```
$ python3.6 swift_challenge.py 20
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
```

## Installing, Testing

Requires Python. Tested with Python 3.6 and 2.7. To set up your testing environment:

1. Create a new virtualenv: `python3.6 -m venv swiftenv`
2. Activate the virtualenv: `source swiftenv/bin/actiavte`
3. Install the py.test package: `pip install -r requirements.txt`

Run the unit tests with `py.test swift_challenge.py -v`.
