# Quize Game using Python

questions = ("What is the fullform of HP: ",
             "Which is the fastest animal in the world: ",
             "How many color are there in rainbow: ",
             "What is the birthday date of Santosh Chapagain: ",
             "How many bone are there in human body: ",
             "which is the best character in the Game of Thrones: ",
             "which is the best character in the Money Heist: ")

options = (("A. High Power","B. Horse Power","C. High Potential","D. High Post"),
           ("A. Lion","B. Chetaah","C. Horse","D. Fox"),
           ("A. 7","B. 6","C. 5","D. 4"),
           ("A. October","B. November","C. December","D. April"),
           ("A. 106","B. 306","C. 206","D. 207"),
           ("A. Jon Snow","B. Bryan Stark","C. Sansa Stark","D. Night King"),
           ("A. Professor","B. Denver","C. Tokiyo","D. Berlin"))

answers = ("B", "B", "A", "C", "D", "B", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("----------------------")
print("       RESULTS        ")
print("----------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")
