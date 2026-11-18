# ruff: file-ignore[suspicious-non-cryptographic-random-usage]

import random

import brain_games.engine as run


def is_prime(num):
    count = 0
    for i in range(1, (num // 2) + 1):
        if num % i == 0:
            count += 1
    if count == 1:
        return "yes"
    return "no"


def generate_rand_num():
    num = random.randrange(1, 150)
    return num, is_prime(num)


def run_game():
    rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    run.play(rules, generate_rand_num)