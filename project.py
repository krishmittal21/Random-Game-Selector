import random
import tkinter as tk
import requests

games = ['completelyrics', 'tictactoe', 'quiz']

def run_random_game():
    game = random.choice(games)
    if game == 'completelyrics':
        completelyrics()
    elif game == 'tictactoe':
        tictactoe()
    elif game == 'quiz':
        quiz()

def main():
    root = tk.Tk()
    root.title("Random Game")
    root.geometry("200x100")

    btn = tk.Button(root, text="Play Random Game", command=run_random_game)
    btn.pack()

    root.mainloop()
def tictactoe():
    board = {
        'T1': ' ', 'T2': ' ', 'T3': ' ',
        'M1': ' ', 'M2': ' ', 'M3': ' ',
        'D1': ' ', 'D2': ' ', 'D3': ' '
    }

    player = 1
    total_moves = 0
    end_check = 0
    high = 0

    def check():
        if board['T1'] == 'X' and board['T2'] == 'X' and board['T3'] == 'X':
            print('Player one won !')
            return 1
        if board['M1'] == 'X' and board['M2'] == 'X' and board['M3'] == 'X':
            print('Player One Won!!')
            return 1
        if board['D1'] == 'X' and board['D2'] == 'X' and board['D3'] == 'X':
            print('Player One Won!!')
            return 1
        if board['T1'] == 'X' and board['M2'] == 'X' and board['D3'] == 'X':
            print('Player One Won!!')
            return 1
        if board['T1'] == 'X' and board['M1'] == 'X' and board['D1'] == 'X':
            print('Player One Won!!')
            return 1
        if board['T2'] == 'X' and board['M2'] == 'X' and board['D2'] == 'X':
            print('Player One Won!!')
            return 1
        if board['T3'] == 'X' and board['M3'] == 'X' and board['D3'] == 'X':
            print('Player One Won!!')
            return 1
        if board['T1'] == 'O' and board['T2'] == 'O' and board['T3'] == 'O':
            print('Player Two Won!!')
            return 1
        if board['M1'] == 'O' and board['M2'] == 'O' and board['M3'] == 'O':
            print('Player Two Won!!')
            return 1
        if board['D1'] == 'O' and board['D2'] == 'O' and board['D3'] == 'O':
            print('Player Two Won!!')
            return 1
        if board['T1'] == 'O' and board['M2'] == 'O' and board['D3'] == 'O':
            print('Player Two Won!!')
            return 1
        if board['T1'] == 'O' and board['M1'] == 'O' and board['D1'] == 'O':
            print('Player Two Won!!')
            return 1
        if board['T2'] == 'O' and board['M2'] == 'O' and board['D2'] == 'O':
            print('Player Two Won!!')
            return 1
        if board['T3'] == 'O' and board['M3'] == 'O' and board['D3'] == 'O':
            print('Player Two Won!!')
            return 1
        return 0

    print('T1|T2|T3')
    print('- +- +-')
    print('M1|M2|M3')
    print('- +- +-')
    print('D1|D2|D3')
    print('***************************')

    while 0 < 1:
        print(board['T1'] + '|' + board['T2'] + '|' + board['T3'])
        print('-+-+-')
        print(board['M1'] + '|' + board['M2'] + '|' + board['M3'])
        print('-+-+-')
        print(board['D1'] + '|' + board['D2'] + '|' + board['D3'])
        end_check = check()
        if total_moves == 9 or end_check == 1:
            break
        while True:
            if player == 1:
                p1_input = input('player one')
                if p1_input.upper() in board and board[p1_input.upper()] == ' ':
                    board[p1_input.upper()] = 'X'
                    player = 2
                    break
                else:
                    print('Invalid input, please try again')
                    continue
            else:
                p2_input = input('player two')
                if p2_input.upper() in board and board[p2_input.upper()] == ' ':
                    board[p2_input.upper()] = 'O'
                    player = 1
                    break
                else:
                    print('Invalid input, please try again')
                    continue
        total_moves += 1
        print('***************************')
        print()
def quiz():
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
            return results
        else:
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

    def main():
        print("Welcome to the Quiz Game!")
        play_quiz_game()

    if __name__ == "__main__":
        main()
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

                # Compare the completion with the actual lyrics
                if completion.lower() in lyrics.lower():
                    print("Correct!")
                else:
                    print("Incorrect!")
            else:
                print("No lyrics found for the specified artist and song.")

        def main():
            print("Welcome to the Complete the Lyrics Game!")
            play_complete_lyrics_game()

        if __name__ == "__main__":
            main()


if __name__ == "__main__":
    main()
