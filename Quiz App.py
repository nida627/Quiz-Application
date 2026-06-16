# Quiz Application

students = {}


def take_quiz():
    name = input("Enter your name: ")

    questions = {
    "Which keyword is used to define a function in Python?": {
        "a": "function",
        "b": "def",
        "c": "func",
        "d": "define",
        "answer": "b"
    },

    "Which symbol is used for comments in Python?": {
        "a": "//",
        "b": "/* */",
        "c": "#",
        "d": "&",
        "answer": "c"
    },

    "Which data type is used to store multiple items in Python?": {
        "a": "int",
        "b": "float",
        "c": "list",
        "d": "string",
        "answer": "c"
    },

    "Which function is used to take input from the user?": {
        "a": "print()",
        "b": "input()",
        "c": "scan()",
        "d": "read()",
        "answer": "b"
    },

    "What is the output of print(type(10))?": {
        "a": "<class 'float'>",
        "b": "<class 'string'>",
        "c": "<class 'int'>",
        "d": "<class 'number'>",
        "answer": "c"
    },

}

    score = 0

    print("\n===== Quiz Started =====")

    for question, data in questions.items():
        print("\n" + question)

        print("a.", data["a"])
        print("b.", data["b"])
        print("c.", data["c"])
        print("d.", data["d"])

        answer = input("Enter your answer (a/b/c/d): ").lower()

        if answer == data["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Wrong!")
            print("Correct answer is:", data["answer"])

    students[name] = score

    print("\nQuiz Completed!")
    print("Your Score:", score, "/", len(questions))


def view_result():
    name = input("Enter your name: ")

    if name in students:
        print(f"{name}'s Score:", students[name])
    else:
        print("Student not found.")


def all_results():
    if len(students) == 0:
        print("No student has taken the quiz yet.")
    else:
        print("\n===== All Student Results =====")

        for name, score in students.items():
            print(f"{name} : {score} Marks")


while True:
    print("\n===== Quiz Application =====")
    print("1. Take Quiz")
    print("2. View My Result")
    print("3. View All Results")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        take_quiz()

    elif choice == "2":
        view_result()

    elif choice == "3":
        all_results()

    elif choice == "4":
        print("Thank You!")
        break

    else:
        print("Invalid Choice.")