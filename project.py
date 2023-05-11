import random
import tkinter as tk
import requests

games = ['completelyrics', 'tictactoe', 'quiz']


def main():
    root = tk.Tk()
    root.title("Random Game")
    root.geometry("200x100")

    btn = tk.Button(root, text="Play Random Game", command=run_random_game)
    btn.pack()

    root.mainloop()


def run_random_game():
    game = random.choice(games)
    if game == 'completelyrics':
        completelyrics()
    elif game == 'tictactoe':
        tictactoe()
    elif game == 'quiz':
        quiz()


def tictactoe():
    board = {
        'T1': ' ', 'T2': ' ', 'T3': ' ',
        'M1': ' ', 'M2': ' ', 'M3': ' ',
        'D1': ' ', 'D2': ' ', 'D3': ' '
    }

    player = 1
    total_moves = 0
    end_check = 0

    def check():
        winning_combinations = [
            ['T1', 'T2', 'T3'],
            ['M1', 'M2', 'M3'],
            ['D1', 'D2', 'D3'],
            ['T1', 'M2', 'D3'],
            ['T1', 'M1', 'D1'],
            ['T2', 'M2', 'D2'],
            ['T3', 'M3', 'D3'],
            ['T1', 'M2', 'D3']
        ]

        for combination in winning_combinations:
            if board[combination[0]] == board[combination[1]] == board[combination[2]] != ' ':
                return True

        return False

    print('T1|T2|T3')
    print('- +- +-')
    print('M1|M2|M3')
    print('- +- +-')
    print('D1|D2|D3')
    print('***************************')

    while True:
        print(board['T1'] + '|' + board['T2'] + '|' + board['T3'])
        print('-+-+-')
        print(board['M1'] + '|' + board['M2'] + '|' + board['M3'])
        print('-+-+-')
        print(board['D1'] + '|' + board['D2'] + '|' + board['D3'])
        end_check = check()

        if total_moves == 9 or end_check:
            break

        while True:
            if player == 1:
                player_input = input('Player one: ')
            else:
                player_input = input('Player two: ')

            if player_input in board and board[player_input] == ' ':
                board[player_input] = 'X' if player == 1 else 'O'
                player = 2 if player == 1 else 1
                total_moves += 1
                break
            else:
                print('Invalid input, please try again')

        print('***************************')
        print()

    if end_check:
        print('Player', player, 'won!')
    else:
        print('It\'s a draw!')


def quiz():
    API_BASE_URL = "https://opentdb.com/api.php"
    API_AMOUNT = 5
    API_CATEGORY = 9
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
            return results
        else:
            print("Failed to retrieve quiz questions. Please try again.")
            print("Failed to retrieve quiz questions. Please try again.")

    def play_quiz_game():
        questions = get_quiz_questions()
        if questions:
            for question in questions:
                print(question["question"])
                options = random.sample(question["incorrect_answers"], 2)
                options.append(question["correct_answer"])
                random.shuffle(options)

                for i, option in enumerate(options):
                    print(f"{i + 1}. {option}")

                answer = input("Your answer (1-3): ")
                if answer == str(options.index(question["correct_answer"]) + 1):
                    print("Correct!")
                else:
                    print("Incorrect!")
                print()

    print("Welcome to the Quiz Game!")
    play_quiz_game()


def completelyrics():
    API_BASE_URL = "https://api.lyrics.ovh/v1"

    def get_song_lyrics(artist, title):
        endpoint = f"{API_BASE_URL}/{artist}/{title}"
        response = requests.get(endpoint)
        if response.status_code == 200:
            data = response.json()
            lyrics = data.get("lyrics", "")
            return lyrics
        else:
            print("Failed to retrieve song lyrics. Please try again.")

    def play_complete_lyrics_game():
        artist = input("Enter the artist name: ")
        title = input("Enter the song title: ")

        lyrics = get_song_lyrics(artist, title)
        if lyrics:
            print("Complete the lyrics:")
            print(lyrics)
            completion = input("Your answer: ")

            if completion.lower() in lyrics.lower():
                print("Correct!")
            else:
                print("Incorrect!")
        else:
            print("No lyrics found for the specified artist and song.")

    print("Welcome to the Complete the Lyrics Game!")
    play_complete_lyrics_game()


if __name__ == "__main__":
    main()
