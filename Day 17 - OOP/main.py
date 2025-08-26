from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []

for key in question_data:
    text = key["text"]
    answer = key["answer"]
    question = Question(q_text=text,q_answer=answer)
    question_bank.append(question)


quiz_q = QuizBrain(question_bank)

while quiz_q.still_has_questions() is True:
    quiz_q.next_question()

if quiz_q.still_has_questions() is False:
    print("You've completed the quiz!")
    print(f"Your final score is {quiz_q.score}/{len(question_bank)}")


