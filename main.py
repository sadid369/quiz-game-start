from question_model import Question
from data import question_data

question_bank = []

for question in question_data:
    question_text= question['text']
    question_answer= question['answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

for object in range(0, len(question_bank)):
    print(f"Q: {question_bank[object].text} A: {question_bank[object].answer}")