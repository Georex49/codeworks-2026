score = 0

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A) Berlin", "B) Wales", "C) Paris", "D) Rome"],
        "answer": "C"
    },
    {
        "question": "What is the capital of Germany?",
        "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
        "answer": "A"
    },
    {
        "question": "What is the capital of Italy?",
        "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
        "answer": "D"
    }
]

print("Welcome to the quiz! Please answer the following questions:\n")

for q in questions:
    print(q["question"])

    for option in q["options"]:
        print(option)

    response = input("Your answer (A, B, C, or D): ").strip().upper()

    if response == q["answer"]:
        print("Correct!\n")
        score += 1
    else:
        print(f"Incorrect. The correct answer is: {q['answer']}\n")

print("=" * 30)
print(f"Your final score is: {score}/{len(questions)}")