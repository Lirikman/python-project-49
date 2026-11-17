import random

import brain_games.engine as run


def is_even(num: int):
    if num % 2 == 0:
        return 'yes'
    else:
        return 'no'


def generate_rand_num():
    num = random.randrange(0, 200)  # ruff: ignore[suspicious-non-cryptographic-random-usage]
    return num, is_even(num)


def run_game():
    rules = 'Answer "yes" if the number is even, otherwise answer "no".'
    run.play(rules, generate_rand_num)