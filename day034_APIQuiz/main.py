# ------------------------------------------------------
# The Quiz Game
# ------------------------------------------------------
"""
- quiz game with GUI
- computer gives to the user a certain amount of questions
- user have to guess the answer (true/false)
- computer gives a feedback about the answer and calculates the score
- at the end, the final score of the quiz is printed
- trivia questions are requested from https://opentdb.com/api_config.php
"""
# ------------------------------------------------------
# Import libraries
# ------------------------------------------------------
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface
# ------------------------------------------------------

# ------------------------------------------------------
# Run the quiz game
# ------------------------------------------------------
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)
# ------------------------------------------------------

