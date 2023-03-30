import random

# questions and answers
questions = [
    {
        "question": "What is the correct way to define a variable in Python?",
        "options": ["int x = 10;", "x := 10", "x = 10", "let x = 10"],
        "answer": "x = 10"
    },
    {
        "question": "Which of the following is a valid Python data type?",
        "options": ["integer", "float", "double", "decimal"],
        "answer": "float"
    },
    {
        "question": "How do you create a list in Python?",
        "options": ["my_list = (1, 2, 3)", "my_list = [1, 2, 3]", "my_list = {1, 2, 3}", "my_list = <1, 2, 3>"],
        "answer": "my_list = [1, 2, 3]"
    },
    {
        "question": "Which loop continues executing a block of code as long as a specified condition is true?",
        "options": ["do-while loop", "for loop", "while loop", "until loop"],
        "answer": "while loop"
    },
    {
        "question": "What is the correct way to define a function in Python?",
        "options": ["function my_function():", "def my_function():", "func my_function():", "define my_function():"],
        "answer": "def my_function():"
    },
    {
        "question": "Which of the following is a valid string in Python?",
        "options": ['"Hello, World!"', "'Hello, World!'", "Hello, World!", "string('Hello, World!')"],
        "answer": "'Hello, World!'"
    },
    {
        "question": "Which of the following is NOT a valid way to create a dictionary in Python?",
        "options": ["my_dict = dict()", "my_dict = {}", "my_dict = {key: value}", "my_dict = [key: value]"],
        "answer": "my_dict = [key: value]"
    },
    {
        "question": "How do you access the first element of a list named 'my_list'?",
        "options": ["my_list[0]", "my_list(0)", "my_list(1)", "my_list[1]"],
        "answer": "my_list[0]"
    },
]

def ask_question(question):
    print(question["question"])
    for i, option in enumerate(question["options"]):
        print(f"{i+1}. {option}")
    answer = int(input("Select the correct option (1-4): ")) - 1
    return question["options"][answer] == question["answer"]

def main():
    score = 0
    random.shuffle(questions)

    for question in questions:
        if ask_question(question):
            print("Correct!")
            score += 1
        else:
            print("Incorrect. Better luck next time!")
        print()

    print(f"Your final score: {score}/{len(questions)}")
    class Question:
    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer

question_pool = [
    Question("What is the correct way to define a variable in Python?", ["int x = 10;", "x := 10", "x = 10", "let x = 10"], "x = 10"),
    # Add more questions related to Python fundamentals as instances of the Question class
]

def ask_question(question):
    print(question.question)
    for i, option in enumerate(question.options):
        print(f"{i+1}. {option}")
    answer = int(input("Select the correct option (1-4): ")) - 1
    return question.options[answer] == question.answer

def main():
    score = 0
    random.shuffle(question_pool)

    for question in question_pool:
        if ask_question(question):
            print("Correct!")
            score += 1
        else:
            print("Incorrect. Better luck next time!")
        print()

    print(f"Your final score: {score}/{len(question_pool)}")

if __name__ == "__main__":
    main()
