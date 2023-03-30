import random

# Sample questions and answers
questions = [
    {
        "question": "What is the correct way to define a variable in Python?",
        "options": ["int x = 10;", "x := 10", "x = 10", "let x = 10"],
        "answer": "x = 10"
    },
    # Add more questions related to Python fundamentals
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

if __name__ == "__main__":
    main()
