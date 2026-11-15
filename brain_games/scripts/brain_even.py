import random, prompt

def random_num():
    return random.randint(1, 100)

def is_even(num: int):
    return num % 2 == 0

def game_even():
    name = prompt.string("Welcome to the Brain Games!\nMay I have your name? ")
    print('''Hello, {name}!
    Answer "yes" if the number is even, otherwise answer "no".''')
    for i in range(3):
        rand_num = random_num()
        print(f"Question: {rand_num}")
        answer = prompt.string("Your answer: ")
        if is_even(random_num):
            if answer == "yes":
                print("Correct!")
                continue
            else:
                print(f"'yes' is wrong answer ;(. Correct answer was 'no'\nLets's try again, {name}!")
                return
        if not is_even(random_num):
            if answer == "no":
                print("Correct!")
                continue
            else:
                print(f"'no' is wrong answer ;(. Correct answer was 'yes'\nLets's try again, {name}!")
    print(f"Congratulations, {name}")