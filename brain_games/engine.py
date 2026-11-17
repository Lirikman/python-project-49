import prompt


def welcome_user():
    name = prompt.string("Welcome to the Brain Games!\nMay I have your name? ")
    print(f"Hello, {name}!")
    return name


def get_answer(question):
    print(f"Question: {question}")
    answer = prompt.string("Your answer: ")
    return answer


def check_answer(user_ans, correct_ans, name):
    if user_ans == str(correct_ans):
        print("Correct!")
        return True
    else:
        print(f"'{user_ans}' is wrong answer ;(. Correct answer was '{correct_ans}'.")
        print(f"Let's try again, {name}!")
        return False


def play(rules, gen_func):
    name = welcome_user()
    print(rules)
    for _ in range(3):
        exp, res = gen_func()
        answer = get_answer(exp)
        ok = check_answer(answer, res, name)
        if not ok:
            return
    print(f"Congratulations, {name}!")
