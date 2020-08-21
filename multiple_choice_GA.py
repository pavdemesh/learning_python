# Multiple Choice game from: https://www.mikedane.com/programming-languages/python/building-a-quiz/
# Youtube Tutorial at: https://youtu.be/rfscVS0vtbw

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


# Define a list with questions and answer options
# Each element (= each question prompt) is a string
question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b)Orange\n",
    "What color are bananas?\n(a) Red/Green\n(b)Yellow\n",
    "Who framed Rabbit Roger?\n(a) Franco\n(b) Jango\n"
]

# Create objects of the class Question and store them as elements of a list
questions_list = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "b")
]


def run_quiz(questions_list_):
    score = 0
    # Iterate through every element in the (questions_list)
    # Every element is an instance of the class Question
    # i.e. (question.answer) and (question.prompt) are available
    for question in questions_list_:
        # For the first object (index[0] in the questions_list)
        # the prompt would be
        # "What color are apples?\n(a) Red/Green\n(b)Orange\n"
        # Then, we store the user's input to this question as (answer)
        answer = input(question.prompt)
        # Compare (answer) and the attribute (.answer) of the corresponding object (question)
        # From the questions_list
        if answer == question.answer:
            score += 1
    print("you got", score, "out of", len(questions_list_))


run_quiz(questions_list)
