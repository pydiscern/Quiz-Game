# Our interactive quiz game will sport the following bells and whistles to keep things exciting:
#
# Rounds: Picture the game as a rollercoaster ride with multiple exhilarating rounds, each presenting a new,
# brain-tickling question to the player.
#
# Question types: To keep you on your toes, questions come in various flavors—multiple-choice, true or false, or
# fill-in-the-blank—making every moment a delightful surprise.
#
# Scoring system: Think of points as shiny gold stars awarded for correct answers, with trickier questions showering
# players with even more sparkling rewards.
#
# Unique features: To crank up the excitement, we'll add a ticking timer to get your adrenaline pumping and throw in
# lifelines as trusty sidekicks for when players find themselves in a pickle.
#
# The game's like a chameleon, adapting to the player's skill level by offering a medley of difficulty levels,
# ensuring barrels of laughs and challenges for everyone!

import random
import time

class Question:
    def __init__(self, question, choices, answer, question_type, difficulty):
        self.question = question
        self.choices = choices
        self.answer = answer
        self.question_type = question_type
        self.difficulty = difficulty

def present_question(question):
    print(question.question)

    if question.choices:
        for i, choice in enumerate(question.choices, 1):
            print(f"{i}. {choice}")

    user_answer = input("Your answer: ")

    if user_answer.lower() == question.answer.lower():
        return True
    else:
        return False

def quiz_game():
    quiz_data = [
        Question("1. What is the output of print(1 + 2)?", ["3", "1", "2"], "3", "multiple_choice", 1),
        Question("2. Which of the following is a valid variable name?", ["1variable", "_variable", "variable!"],
                 "_variable", "multiple_choice", 1),
        Question("3. What is the output of the following code?\nprint(type(3.14))",
                 ["<class 'float'>", "<class 'int'>", "<class 'str'>"], "<class 'float'>", "multiple_choice", 1),
        Question("4. What is the output of print(5 // 2)?", ["2.5", "2", "3"], "2", "multiple_choice", 1),
        Question("5. Which keyword is used to define a function in Python?", ["func", "def", "function"], "def",
                 "multiple_choice", 1),
        Question("6. Which keyword is used to create a class in Python?", ["class", "object", "def"], "class",
                 "multiple_choice", 1),
        Question("7. How do you create a list in Python?",
                 ["Using brackets []", "Using parentheses ()", "Using curly braces {}"], "Using brackets []",
                 "multiple_choice", 1),
        Question("8. How do you add an element to a list in Python?", ["append()", "add()", "push()"], "append()",
                 "multiple_choice", 1),
        Question("9. How do you remove an element from a list in Python?", ["remove()", "pop()", "delete()"],
                 "remove()", "multiple_choice", 1),
        Question("10. What is the difference between a tuple and a list in Python?",
                 ["Tuples are immutable, lists are mutable", "Lists are immutable, tuples are mutable",
                  "Tuples are indexed, lists are not"], "Tuples are immutable, lists are mutable", "multiple_choice",
                 1),
        Question("11. How do you create a dictionary in Python?",
                 ["Using brackets []", "Using parentheses ()", "Using curly braces {}"], "Using curly braces {}",
                 "multiple_choice", 1),
        Question("12. How do you access the value of a key in a dictionary?",
                 ["dict[key]", "dict.value(key)", "dict.get(key)"], "dict[key]", "multiple_choice", 1),
        Question("13. What is the output of the following code? print('Hello, World!'.lower())",
                 ["hello, world!", "HELLO, WORLD!", "hELLO, wORLD!"], "hello, world!", "multiple_choice", 1),
        Question("14. How do you import a module in Python?",
                 ["import module", "from module import *", "require module"],
                 "import module", "multiple_choice", 1),
        Question("15. What is the output of the following code? print(2 ** 3)", ["6", "8", "9"], "8", "multiple_choice",
                 1),
        Question("16. What is the purpose of a 'for' loop in Python?",
                 ["To iterate over a sequence", "To check a condition", "To delay execution"],
                 "To iterate over a sequence",
                 "multiple_choice", 1),
        Question("17. What is the purpose of a 'while' loop in Python?",
                 ["To iterate over a sequence", "To check a condition", "To delay execution"], "To check a condition",
                 "multiple_choice", 1),
        Question("18. How do you create a multi-line comment in Python?",
                 ["Using //", "Using /* */", "Using ''' or \""""],
                 "Using ''' or \"", "multiple_choice", 1),
        Question("19. What is the difference between a global and a local variable in Python?",
                 ["Global variables are declared outside a function, local variables are declared inside a function",
                  "Global variables are declared inside a function, local variables are declared outside a function",
                  "There is no difference"],
                 "Global variables are declared outside a function, local variables are declared inside a function",
                 "multiple_choice", 1),
        Question("20. What is the output of the following code? print('Python'[::-1])", ["nohtyP", "nhotyP", "Python"],
                 "nohtyP", "multiple_choice", 1),
        Question("21. What is the output of the following code? print('3' + '5')", ["8", "35", "53"], "35",
                 "multiple_choice", 1),
        Question("22. What is the purpose of the 'pass' keyword in Python?",
                 ["To skip an iteration", "To break out of a loop", "To indicate an empty block of code"],
                 "To indicate an empty block of code", "multiple_choice", 1),
        Question("23. How do you create a set in Python?",
                 ["Using parentheses ()", "Using brackets []", "Using curly braces {}"], "Using curly braces {}",
                 "multiple_choice", 1),
        Question("24. What is the output of the following code? print(3 * 'A' + 'B')",
                 ["AAAB", "AAB", "AAAAB"],"AAAB", "multiple_choice", 1),
        Question("25. What is the output of the following code? print(10 % 3)", ["1", "3", "0"], "1","multiple_choice", 1),
        Question("26. What is the purpose of the 'break' keyword in Python?",
                          ["To skip an iteration", "To break out of a loop", "To indicate an empty block of code"],
                          "To break out of a loop", "multiple_choice", 1),
        Question("27. What is the purpose of the 'continue' keyword in Python?",
                          ["To skip an iteration", "To break out of a loop", "To indicate an empty block of code"],
                          "To skip an iteration", "multiple_choice", 1),
        Question("28. Which of the following is a Python built-in function to read input from the user?",
                          ["read()", "input()", "scan()"], "input()", "multiple_choice", 1),
        Question("29. How do you convert a string to an integer in Python?",
                          ["int(string)", "string.toInt()", "parseInt(string)"], "int(string)", "multiple_choice", 1),
        Question("30. How do you handle exceptions in Python?", ["try-except", "catch-throw", "if-else"],
                          "try-except", "multiple_choice", 1),
        Question("31. What is the output of the following code? print(len('Python'))", ["5", "6", "7"], "6",
                          "multiple_choice", 1),
        Question("32. Which method is used to find the index of a specific element in a list?",
                          ["find()", "search()", "index()"], "index()", "multiple_choice", 1),
        Question("33. What is the output of the following code? print('Python'.upper())",
                          ["PYTHON", "python", "Python"], "PYTHON", "multiple_choice", 1),
        Question("34. Which of the following is not a valid comparison operator in Python?", ["==", "is", "="],
                          "=", "multiple_choice", 1),
        Question("35. How do you check if an element is present in a list?", ["in", "contains", "has"], "in",
                          "multiple_choice", 1),
        Question("36. What is the output of the following code? print(list(range(3)))",
                          ["[0, 1, 2]", "[1, 2, 3]", "[0, 1, 2, 3]"], "[0, 1, 2]", "multiple_choice", 1),
        Question("37. What is the output of the following code? print('\\n'.join(['A', 'B', 'C']))",
                          ["A\nB\nC", "A B C", "ABC"], "A\nB\nC", "multiple_choice", 1),
        Question("38. Which of the following is not a valid assignment operator in Python?", ["=", "+=", "=+"],
                          "=+", "multiple_choice", 1),
        Question("39. Which of the following is a valid method to remove an element from a set?",
                          ["discard()", "remove()", "pop()"], "discard()", "multiple_choice", 1),
        Question("40. What is the output of the following code? print(2 + 3 * 4)", ["20", "14", "10"], "14",
                          "multiple_choice", 1),
        Question("41. Which of the following is a Python built-in function to round a number to the nearest integer?",
                     ["round()", "math.round()", "math.ceil()"], "round()", "multiple_choice", 1),
        Question("42. What is the output of the following code? print(10 / 2)", ["5", "5.0", "4"], "5.0",
                          "multiple_choice", 1),
        Question("43. Which of the following is a valid method to sort a list in Python?",
                          ["sort()", "sorted()", "list.sort()"], "sorted()", "multiple_choice", 1),
        Question("44. What is the output of the following code? print('hello'.replace('l', 'L'))",
                          ["heLLo", "HELLO", "hELLO"], "heLLo", "multiple_choice", 1),
        Question("45. Which of the following is a Python built-in function to get the ASCII value of a character?",
                     ["ord()", "ascii()", "chr()"], "ord()", "multiple_choice", 1),
        Question("46. Which of the following is a valid method to create a lambda function in Python?",
                          ["lambda x: x * 2", "x => x * 2", "def(x): x * 2"], "lambda x: x * 2", "multiple_choice", 1),
        Question("47. What is the output of the following code? print('Python'.startswith('P'))",
                          ["True", "False", "None"],
                          "True", "multiple_choice", 1),
        Question("48. What is the output of the following code? print('3.14'.isdigit())",
                          ["True", "False", "None"],
                          "False", "multiple_choice", 1),
        Question("49. Which of the following is a valid method to create a file in Python?",
                          ["open('file.txt', 'w')", "create('file.txt')", "file.new('file.txt')"],
                          "open('file.txt', 'w')",
                          "multiple_choice", 1),
        Question("50. What is the output of the following code? print('Hello, {0}!'.format('World'))",
                          ["Hello, {0}!", "Hello, World!", "Hello, {World}!"], "Hello, World!", "multiple_choice", 1)
    ]
    total_questions = len(quiz_data)
    score = 0

    print("Welcome to the interactive quiz game!")
    print("You will be presented with questions of various types.")
    print("Answer correctly to earn points. Good luck!\n")

    order_choice = input("Choose the order of questions: (C)hronological or (R)andom: ").lower()
    while order_choice not in ['c', 'r']:
        order_choice = input("Invalid choice. Please choose (C)hronological or (R)andom: ").lower()

    if order_choice == 'r':
        random.shuffle(quiz_data)

    for i in range(total_questions):
        print(f"Round {i + 1} of {total_questions}")
        question = quiz_data[i]

        start_time = time.time()
        timer = 30

        if present_question(question):
            score += 1
            print("Correct! Your score:", score)
        else:
            print("Incorrect. The correct answer is:", question.answer)

        print("Time remaining:", timer - int(time.time() - start_time), "seconds\n")

    print("Game over. Your final score:", score)

if __name__ == "__main__":
    quiz_game()
