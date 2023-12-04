class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self):
        if self.question_number != len(self.question_list):
            return True
        else:
            return False

    def check_answer(self, user_ans, correct_ans):
        if user_ans == correct_ans:
            self.score += 1
            print(f"You got it right! \nThe correct answer was: {correct_ans}")
            print(f"Your current score is {self.score}/{self.question_number}")
        else:
            print(f"That is wrong \nThe correct answer was: {correct_ans}")
            print(f"Your current score is {self.score}/{self.question_number}")

    def next_question(self):
        answer = input(f"Q.{self.question_number + 1}: {self.question_list[self.question_number].text} (True/Fale)?: ").lower()
        correct_answer = self.question_list[self.question_number].answer.lower()
        self.question_number += 1
        self.check_answer(answer, correct_answer)
