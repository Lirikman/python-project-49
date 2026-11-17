import random
import prompt


def generate_match_exp():
    num1 = random.randrange(1, 20)
    num2 = random.randrange(1, 20)
    oper = random.choice(['+', '-', '*'])
    exp = f"{num1} {oper} {num2}"
    result = eval(exp)
    return exp, result


def main():
    name = prompt.string("Welcome to the Brain Games!\nMay I have your name? ")
    print(f"Hello, {name}!")
    print("What is the result of the expression?")
    for _ in range(3):

        exp, res = generate_match_exp()
        print(f"Question: {exp}")
        answer = prompt.integer("Your answer: ")
        if res == answer:
            print("Correct!")
            continue
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{res}'.")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")


    if __name__ == "__main__":
        "main()"