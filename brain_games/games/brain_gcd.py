# ruff: file-ignore[suspicious-non-cryptographic-random-usage]

import random

import brain_games.engine as run


def generate_num_and_gcd():
    num1 = random.randrange(1, 50)
    num2 = random.randrange(1, 50)
    a, b = num1, num2
    while b != 0:
        a, b = b, a % b
    return f"{num1} {num2}", a


def run_game():
    rules = "Find the greatest common divisor of given numbers."
    run.play(rules, generate_num_and_gcd)