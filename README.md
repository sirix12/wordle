# Wordle game
#### Description:


Welcome to the Wordle game—a fun and engaging challenge that tests your word-guessing skills. In this game, your objective is to guess a randomly generated word of your chosen length within five attempts. Each guess will give you feedback in the form of color-coded clues to help you refine your guesses.

## Features

- Ability to choose a word length between 3 and 12 letters.
- Colour-coded feedback for each guess:
    - **Green** : Correct letter in the correct position.
    - **Yellow** : Correct letter but in wrong position.
    - **Red** : Incorrect letter.

## Requirements

To run this game, you'll need python 3.x and following libraries:

- `requests`
- `tabulate`
- `termcolor`

install these dependencies using pip3:

```
pip install requests tabulate termcolor
```
## How to play
1. Run the game:
```
python WODL.py
```
2. Select word length:
    - Enter the desired length of the word, which should be between 3 and 12 letters.

3. Make guesses:
    - Enter your guess. Ensure the length of your guess matches the word length you selected. If the length is incorrect, you will be reprompted to enter a valid guess.
    - You have up to 5 attempts to guess the correct word.
4. Game End:
    - If you guessed the correct word within 5 tries game will exit after display "YOU WON!".
    - If you exhaust all 5 attempts without guessing the word, the game will reveal the correct word and then exit.

## Technical details

- `main()`: Runs the main game.
- `get_n` : Prompts the user to select the word length.
- `check(correct_word, user_word)`: Compares the guessed word and correct word and return a list with colored letters according to the correctness of each letter(yellow, green and red)
- `draw_grid(checked)`: display the guessed word in a grid format with colored letters list returned from check().
- `get_guess(n)`: prompt the user for their guess with n number of letters.

### Customization

#### Change the grid style
if you want to change the style of the grid that checked word appears by changing the `tablefmt` parameter in the `draw_grid(checked)` function like "plain", "fancy_grid", and many more as in table format section of [Tabulate homepage](https://pypi.org/project/tabulate/).

#### Change the colours of colored letters
you could change the colours of letters in checked word by replacing the parameters green yellow and red with your desired colours in `check(correct_word, user_word)` function.you can also change the attributes of letters by changing attrs.you can learn more about letters colors and their attributes from text properties section of [termcolor homepage](https://pypi.org/project/termcolor/).

## Test function
To ensure the program functions correctly, use test_WODL.py with pytest to run tests. Execute the following command in your terminal:
```
pytest test_WODL.py
```
The test_WODL.py file includes tests for the get_word(), get_guess(), get_n(), and check() functions. You are encouraged to add additional tests as needed. It is recommended to always run tests after making any modifications to the program to ensure everything is working as expected.
