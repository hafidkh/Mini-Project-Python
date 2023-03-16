questions = [
    {
        "question": "Quelle la capitale de l'algérie ?",
        "reponse": "Alger"
    },
    {
        "question": "Quelle est la voiture la plus rapide au monde ?",
        "reponse": "Bugatti"
    },
    {
        "question": "qui est le fondateur de microsoft ?",
        "reponse": "Bill Gates"
    }
]

score = 0

for question in questions:
    user_answer = input(question["question"] + " ")
    if user_answer.lower() == question["reponse"].lower():
        score += 1
        print("Correct!")
    else:
        print("Incorrect. la reponse correcte est : " + question["reponse"])

print("Votre score est " + str(score) + " sur " + str(len(questions)))