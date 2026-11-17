import random

import operator

import brain_games.engine as run


def generate_match_exp():
    operations = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
    }
    num1 = random.randrange(1, 20)
    num2 = random.randrange(1, 20)
    oper = random.choice(list(operations.keys()))
    exp = f"{num1} {oper} {num2}"
    result = operations[oper](num1, num2)
    return exp, result



def run_game():
    rules = "What is the result of the expression?"
    run.play(rules, generate_match_exp)