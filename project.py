import random
import tkinter as tk
import requests

games = ['tictactoe', 'quiz']


def run_random_game():
    game = random.choice(games)
    if game == 'tictactoe':
        play_tictactoe_game()
    elif game == 'quiz':
        play_quiz_game()


def play_tictactoe_game():
    board = {
        'T1': ' ', 'T2': ' ', 'T3': ' ',
        'M1': ' ', 'M2': ' ', 'M3': ' ',
        'D1': ' ', 'D2': ' ', 'D3': ' '
    }

    player = 'X'
    total_moves = 0
    end_check = False

    def check_winner():
        winning_conditions = [
            ['T1', 'T2', 'T3'], ['M1', 'M2', 'M3'], ['D1', 'D2', 'D3'],
            ['T1', 'M1', 'D1'], ['T2', 'M2', 'D2'], ['T3', 'M3', 'D3'],
            ['T1', 'M2', 'D3'], ['T3', 'M2', 'D1']
        ]
        for condition in winning_conditions:
            if board[condition[0]] == board[condition[1]] == board[condition[2]] != ' ':
                return board[condition[0]]
        return ''

    def handle_click(key):
        nonlocal player, total_moves, end_check
        if not end_check and board[key] == ' ':
            board[key] = player
            buttons[key].config(text=player)
            total_moves += 1

            winner = check_winner()
            if winner:
                result_label.config(text=f"Player {winner} wins!")
                end_check = True
            elif total_moves == 9:
                result_label.config(text="It's a tie!")
                end_check = True
            else:
                player = 'O' if player == 'X' else 'X'

    root = tk.Tk()
    root.title("Tic-Tac-Toe")
    root.geometry("300x300")

    buttons = {}
    row = 0
    col = 0
    for key in board:
        button = tk.Button(root, text=' ', width=10, height=5, command=lambda key=key: handle_click(key))
        button.grid(row=row, column=col)
        buttons[key] = button

        col += 1
        if col > 2:
            col = 0
            row += 1

    result_label = tk.Label(root, text="", pady=10)
    result_label.grid(row=row, columnspan=3)

    root.mainloop()


def play_quiz_game():
    API_BASE_URL = "https://opentdb.com/api.php"
    API_AMOUNT = 5  # Number of questions to retrieve
    API_CATEGORY = 9  # Category ID for General Knowledge
    API_DIFFICULTY = "medium"

    def get_quiz_questions():
        params = {
            "amount": API_AMOUNT,
            "category": API_CATEGORY,
            "difficulty": API_DIFFICULTY,
            "type": "multiple",
        }

        response = requests.get(API_BASE_URL, params=params)
        if response.status_code == 200:
            data = response.json()
            results = data.get("results", [])

            # Add 'correct_answer_index' key to each question
            for question in results:
                correct_index = random.randint(0, 3)
                question['correct_answer_index'] = correct_index

            return results
        else:
            print("Failed to retrieve quiz questions. Please try again.")

    def handle_answer_selection(answer_index, question):
        if answer_index == question["correct_answer_index"]:
            result_label.config(text="Correct!", fg="green")
        else:
            result_label.config(text="Incorrect!", fg="red")

    def display_quiz_question(question):
        question_label.config(text=question["question"])
        answers = question["incorrect_answers"]
        answers.insert(question["correct_answer_index"], question["correct_answer"])

        for i, answer in enumerate(answers):
            button = answer_buttons[i]
            button.config(text=answer)
            button.config(command=lambda index=i, q=question: handle_answer_selection(index, q))

    def next_question():
        nonlocal current_question_index
        current_question_index += 1

        if current_question_index < len(quiz_questions):
            display_quiz_question(quiz_questions[current_question_index])
        else:
            quiz_frame.destroy()
            result_label.config(text="Quiz Completed!")

    quiz_questions = get_quiz_questions()
    if quiz_questions:
        current_question_index = 0

        root = tk.Tk()
        root.title("Quiz Game")
        root.geometry("400x300")

        quiz_frame = tk.Frame(root)
        quiz_frame.pack(pady=10)

        question_label = tk.Label(quiz_frame, text="", wraplength=380)
        question_label.pack(pady=10)

        answer_buttons = []
        for i in range(4):
            button = tk.Button(quiz_frame, text="", width=40, command=lambda: None)
            button.pack(pady=5)
            answer_buttons.append(button)

        result_label = tk.Label(root, text="", pady=10)
        result_label.pack()

        next_button = tk.Button(root, text="Next", command=next_question)
        next_button.pack(pady=10)

        display_quiz_question(quiz_questions[current_question_index])

        root.mainloop()
    else:
        print("Failed to retrieve quiz questions. Please try again.")


def run_game():
    run_random_game()


root = tk.Tk()
root.title("Random Game Selector")
root.geometry("200x100")

button = tk.Button(root, text="Run Random Game", command=run_game)
button.pack(pady=20)

root.mainloop()
