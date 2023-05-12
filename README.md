# Random Game Selector
# Harvard CS50 Projecy
This is a Python script that allows you to play random games. It includes two games: Tic-Tac-Toe and a Quiz game. The script utilizes the tkinter library for creating a graphical user interface and the requests library for making API calls to retrieve quiz questions.

## Installation

To run this script, you need to have Python installed on your system. Additionally, you need to install the following dependencies:

- tkinter: `pip install tkinter`
- requests: `pip install requests`

## Usage

1. Import the required libraries:

```python
import random
import tkinter as tk
import requests
```

2. Define the main function, which sets up the GUI and starts the game selection:

```python
def main():
    root = tk.Tk()
    root.title("Random Game Selector")
    root.geometry("200x100")

    button = tk.Button(root, text="Run Random Game", command=run_game)
    button.pack(pady=20)

    root.mainloop()
```

3. Define the `run_random_game` function, which randomly selects a game and calls the corresponding game function:

```python
def run_random_game():
    games = ['tictactoe', 'quiz']
    game = random.choice(games)
    if game == 'tictactoe':
        play_tictactoe_game()
    elif game == 'quiz':
        play_quiz_game()
```

4. Define the `play_tictactoe_game` function, which implements the Tic-Tac-Toe game:

```python
def play_tictactoe_game():
    # Game logic goes here
```

5. Define the `play_quiz_game` function, which retrieves quiz questions from an API and implements the Quiz game:

```python
def play_quiz_game():
    # Game logic goes here
```

6. Define any additional helper functions required for the games.

7. Define the `run_game` function, which is the entry point for starting a game:

```python
def run_game():
    run_random_game()

if __name__ == "__main__":
    main()
```

8. Run the script:

```shell
python script.py
```

9. Click the "Run Random Game" button to start a randomly selected game.

Note: Ensure that the `API_BASE_URL` constant in the `play_quiz_game` function is correctly set to the desired API endpoint for retrieving quiz questions.

Enjoy playing the random games! 
