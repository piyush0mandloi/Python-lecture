class Questions:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer
    
def run_quiz(questions):
    score = 0
    for q in questions:
        user_answer = input(q.prompt)
        if user_answer.lower() == q.answer.lower():
            score+=1
    print(f"You got {score}/{len(questions)} correct!")

question_prompts = [
    "What is the capital of India?\n(a) Mumbai\n(b) Delhi\n(c) Kolkata\n ",
    "Which language is used build Android apps?\n(a) Java\n(b) Python\n(c) Swift\n ",
    "What does CPU stand for?\n(a) Central Process Unit\n(b) Central Processing Unit\n(c) Computer Personal Unit\n ",
]

questions = [
    Questions(question_prompts[0], "b"),
    Questions(question_prompts[1], "a"),
    Questions(question_prompts[2], "b")
]

run_quiz(questions)