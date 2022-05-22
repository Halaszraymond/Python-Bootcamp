class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        question_text = self.question_list[self.question_number].text.lower()
        correct_answer = self.question_list[self.question_number].answer.lower()
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {question_text} (True/False): ").lower()
        self.check_answer(user_answer, correct_answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            self.score += 1
            print(f"You got it right! The correct score was '{correct_answer}'."
                  f"\nYour current score is {self.score}/{self.question_number}.\n")
        else:
            print(f"That's wrong, the correct answer was '{correct_answer}'."
                  f"\nYour current score is {self.score}/{self.question_number}.\n")





