
# Quiz1.py代码
def quiz():
    print("Welcome to the Animal Quiz!")
    print("Answer the following questions:")
    # Questions and Answers
    questions = [
        "1.What is the largest animal on Earth?:a.Blue Whale,b.Mouse,c.Cat",
        "2.which bird can fly backwards?:a.Cuckoo,b.Eagle,c.Hummingbird",
        "3.What is the only mammal capable of flight?:a.Bat,b.Squirre1,c.Dolphin"
    ]
    answers = [
        "Blue whale",
        "Hummingbird",
        "Bat"
    ]
    score = 0
    # Ask questions
    for i in range(len(questions)):
        user_answer = input(questions[i]).strip().lower()
        if user_answer == answers[i]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
    # Provide final score
    print("\nQuiz completed!")
    print(f"You got {score} / {len(questions)} questions correct.")


# Run the quiz function
quiz()