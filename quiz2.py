# Quiz2.py代码（文档中未完整给出，仅包含题目部分）
# 假设需补充LED控制相关代码，可参考以下框架，需根据实际电路连接调整GPIO引脚编号等细节
import RPi.GPIO as GPIO
import time

# 设置GPIO模式和引脚
GPIO.setmode(GPIO.BCM)
green_led_pin = 17
red_led_pin = 18
GPIO.setup(green_led_pin, GPIO.OUT)
GPIO.setup(red_led_pin, GPIO.OUT)


def quiz():
    print("Welcome to the Quiz!")
    print("Answer the following questions:")
    # Questions and Answers
    questions = [
        "1) Which of the following is NOT a python data type?",
        "2) Which of the following is NOT a built-in operation in Python?",
        "3) In a mixed-type expression involving ints and floats, Python will convert:",
        "4)The best structure for implementing a multi-way decision in Python is:",
        "5)What statement can be executed in the body of a loop to cause it to terminate?"
    ]
    answers = [
        "c",
        "d",
        "d",
        "c",
        "d"
    ]
    score = 0
    # Ask questions
    for i in range(len(questions)):
        print(questions[i])
        print("a) option1")
        print("b) option2")
        print("c) option3")
        print("d) option4")
        user_answer = input().strip().lower()
        if user_answer == answers[i]:
            print("Correct!")
            GPIO.output(green_led_pin, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(green_led_pin, GPIO.LOW)
            score += 1
        else:
            print("Incorrect!")
            GPIO.output(red_led_pin, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(red_led_pin, GPIO.LOW)
    # Provide final score
    print("\nQuiz completed!")
    print(f"You got {score} / {len(questions)} questions correct.")
    GPIO.cleanup()


# Run the quiz function
quiz()