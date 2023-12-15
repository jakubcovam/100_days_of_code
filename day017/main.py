# ------------------------------------------------------
# The Quiz Game
# ------------------------------------------------------
"""
- this game teaches you to use classes and modules in Python
- computer gives to the user a certain amount of guestions
- user have to guess the answer (true/false)
- computer gives a feedback about the answer and calculates the score
- at the end, the final score of the quiz is printed
- trivia questions can be created via https://opentdb.com/api_config.php
"""
# ------------------------------------------------------
# Import libraries
# ------------------------------------------------------
from question_model import Question
from data import question_data, data_trivia
from quiz_brain import QuizBrain
# ------------------------------------------------------

# ------------------------------------------------------
# Run the quiz game
# ------------------------------------------------------
question_bank = []

which_dataset = input("Do you want 'handmade' or 'trivia' data? Type 'h' or 't': ").lower()
if which_dataset == 'h':
    used_data = question_data
else:
    used_data = data_trivia

for question in used_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# print(question_bank)
# print(question_bank[0].text)
# print(question_bank[0].answer)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz.")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")

# ------------------------------------------------------
