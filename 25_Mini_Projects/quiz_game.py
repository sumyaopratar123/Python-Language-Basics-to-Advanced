# Python Basics to Advanced Example
# Run: python quiz_game.py

questions = [("What is 2 + 2?", "4"), ("Which keyword defines a function?", "def"), ("What type is True?", "bool")]
score = 0
for question, answer in questions:
    if input(question + " ").strip().casefold() == answer.casefold():
        print("Correct!"); score += 1
    else: print("Answer:", answer)
print(f"Score: {score}/{len(questions)}")
