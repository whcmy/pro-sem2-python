import RPi.GPIO as GPIO
import time


def quiz():
    print("Welcome to the Quiz!")
    print("Answer the following questions:")
    # 问题和答案
    questions = [
        "1) Which of the following is NOT a python data type?",
        "2) Which of the following is NOT a built-in operation in Python?",
        "3) In a mixed-type expression involving ints and floats, Python will convert:",
        "4)The best structure for implementing a multi-way decision in Python is:",
        "5)What statement can be executed in the body of a loop to cause it to terminate?"
    ]
    options = [
        ["a) int", "b) float", "c) rational", "d) string", "e) bool"],
        ["a)+", "b)%", "c) abs()", "d) sqto"],
        ["a) floats to ints", "b) ints to strings", "c) floats and ints to strings", "d) ints to floats"],
        ["a) if", "b) if-else", "c) if-elif-else", "d) try"],
        ["a) if", "b) exit", "c) continue", "d) break"]
    ]
    answers = ["c", "d", "d", "c", "d"]
    score = 0

    # 设置GPIO模式和引脚
    GPIO.setmode(GPIO.BCM)
    green_led_pin = 17
    red_led_pin = 18
    GPIO.setup(green_led_pin, GPIO.OUT)
    GPIO.setup(red_led_pin, GPIO.OUT)

    # 提问
    for i in range(len(questions)):
        print(questions[i])
        for option in options[i]:
            print(option)
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

    # 给出最终分数
    print("\nQuiz completed!")
    print(f"You got {score} / {len(questions)} questions correct.")
    GPIO.cleanup()


# 运行问答函数
quiz()