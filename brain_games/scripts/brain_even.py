import random

import prompt


def random_num():
    return random.randrange(0, 200)  # ruff: ignore[suspicious-non-cryptographic-random-usage]


def is_even(num: int):
    return num % 2 == 0


def main():
    name = prompt.string("Welcome to the Brain Games!\nMay I have your name? ")
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(3):
        num = random_num()
        print(f"Question: {num}")
        answer = prompt.string("Your answer: ")
        if is_even(num):
            if answer == "yes":
                print("Correct!")
                continue
            else:
                print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'.")
                print(f"Lets's try again, {name}!")
                return
        if not is_even(num):
            if answer == "no":
                print("Correct!")
                continue
            else:
                print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'.")
                print(f"Lets's try again, {name}!")
                return
    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    "main()"