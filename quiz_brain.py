class QuizBrain:

    # Constructor
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.user_score = 0

    def still_has_questions(self):
        total_questions = len(self.question_list)
        return self.question_number != total_questions

    def next_question(self):
        current_question = self.question_list[self.question_number]
        user_answer = input(f"Q.{self.question_number + 1}: {current_question.text} (True/False)?: ")
        self.question_number += 1
        self.check_answrer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer[0].lower() == correct_answer[0].lower():
            print("You got it right!")
            self.user_score += 1
        else:
            print("That is wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.user_score}/{self.question_number}.")
        print("\n")




