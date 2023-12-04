from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

questions_bank = []

for i in range(0, len(question_data)):
    questions_bank.append(Question(question_data[i]["text"], question_data[i]["answer"]))


brain = QuizBrain(questions_bank)

while brain.still_has_question():
    brain.next_question()
