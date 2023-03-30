import random
import time

class Question:
    def __init__(self, question, choices, correct_answer):
        self.question = question
        self.choices = choices
        self.correct_answer = correct_answer

question_pool = [
    Question("What is the output of print(1 + 2)?", ["3", "1", "2"], "3"),
    Question("Which of the following is a valid variable name?", ["1variable", "_variable", "variable!"], "_variable"),
    Question("What is the output of the following code?\nprint(type(3.14))", ["<class 'float'>", "<class 'int'>", "<class 'str'>"], "<class 'float'>"),
    Question("What is the output of print(5 // 2)?", ["2.5", "2", "3"], "2"),
    Question("Which keyword is used to define a function in Python?", ["func", "def", "function"], "def"),
    Question("Which data structure is used to store key-value pairs in Python?", ["List", "Tuple", "Dictionary"], "Dictionary"),
    Question("How do you create a list with the values 1, 2, 3?", ["list(1, 2, 3)", "[1, 2, 3]", "{1, 2, 3}"], "[1, 2, 3]"),
    Question("What is the output of the following code?\nprint('Hello, ' + 'World!')", ["Hello, World!", "Hello,  World!", "SyntaxError"], "Hello, World!"),
    Question("Which of the following is NOT a valid comparison operator in Python?", ["==", "<>", "<="], "<>"),
    Question("What is the output of the following code?\nprint('Python'.upper())", ["PYTHON", "python", "Python"], "PYTHON"),
    Question("Which loop continues to execute as long as the condition is True?", ["for loop", "while loop", "do-while loop"], "while loop"),
    Question("What is the output of the following code?\nprint('Hello\\nWorld')", ["Hello\nWorld", "Hello\\nWorld", "Hello World"], "Hello\\nWorld"),
    Question("Which of the following is a Python comment?", ["// This is a comment", "# This is a comment", "/* This is a comment */"], "# This is a comment"),
    Question("Which function is used to get input from the user?", ["input()", "get_input()", "read()"], "input()"),
    Question("What is the output of the following code?\nprint(3 ** 2)", ["9", "6", "1"], "9"),
]

def display_question(question):
    print(question.question)
    for idx, choice in enumerate(question.choices):
        print(f"{idx + 1}. {choice}")

def get_user_input():
    return input("Enter your answer: ")

def evaluate_response(user_response, correct_answer):
    return user_response == correct_answer

def play_game():
    score = 0
    while True:
        question = random.choice(question_pool)
        display_question(question)
        user_response = get_user_input()
        if evaluate_response(user_response, question.correct_answer):
            score += 1
            print("Correct!")
        else:
            print(f"Sorry, the correct answer is {question.correct_answer}.")
        
        print(f"Your score: {score}")
        play_again = input("Do you want to play again? (Y/N) ")
        if play_again.lower() != 'y':
            break

if __name__ == "__main__":
    play_game()
